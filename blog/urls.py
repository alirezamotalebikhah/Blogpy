from django.urls import path
from . import views

urlpatterns =[
    path('', views.IndexPage.as_view(), name='index'),
    path('article/' , views.SingleArticleAPIView.as_view(), name='single_article'),
    path('article/all/', views.AllArticleAPIView.as_view(), name='all_articles'),
]