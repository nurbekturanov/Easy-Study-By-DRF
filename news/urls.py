from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.NewsList.as_view(), name='news_list'),
    path('news/<pk>/', views.NewsDetail.as_view(), name='news_detail'),
]
