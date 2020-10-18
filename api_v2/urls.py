from django.urls import path

from api_v2.views import get_token_view, ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView

app_name = 'api_v2'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_view'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete')
]