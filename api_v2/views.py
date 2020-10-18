from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404
import json

# Create your views here.
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleListSerializer, ArticleDetailSerializer, ArticleSerializer
from webapp.models import Article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ArticleListView(APIView):
    def get(self, request):
        objects = Article.objects.all()
        slr = ArticleListSerializer(objects, many=True)
        return Response(slr.data)

# class ArticleListView(View):
#     def get(self, request, *args, **kwargs):
#         objects = Article.objects.all()
#         slr = ArticleListSerializer(objects, many=True)
#         return JsonResponse(slr.data, safe=False)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        objects = Article.objects.get(id=pk)
        slr = ArticleDetailSerializer(objects)
        return Response(slr.data)


class ArticleUpdateView(APIView):
    def put(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        data = json.loads(request.body)
        slr = ArticleSerializer(instance=article, data=data, partial=True)
        if slr.is_valid(raise_exception=True):
            article = slr.save()
            return Response(slr.data)
        else:
            return Response({
                "error": "Произошла ошибка"
            })


class ArticleDeleteView(APIView):
    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response(pk)


class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        slr = ArticleListSerializer(data=data)
        if slr.is_valid():
            article = slr.save()
            return JsonResponse(slr.data, safe=False)
        else:
            response = JsonResponse(slr.errors, safe=False)
            response.status_code = 400
            return response
