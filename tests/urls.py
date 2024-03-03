from django.urls import path

from . import views

urlpatterns = [
    path('tests/', views.CategoryList.as_view(), name="subject_list"),
    path("tests/<str:slug>/", views.QuestionList.as_view(), name='test_list'),
    path('tests/<str:slug>/<int:pk>/', views.QuestionDetail.as_view(), name='test_detail'),
]
