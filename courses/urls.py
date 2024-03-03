from django.urls import path

from . import views


urlpatterns = [
    path('courses/', views.CourseModuleList.as_view(), name='course_module_list'),
    # path('<pk>/', views.CourseModuleDetail.as_view(), name='course_module_detail'),
    path('courses/<str:slug>/', views.CourseList.as_view(), name='course_list'),
    path('courses/<str:slug>/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('courses/<str:slug>/<int:pk>/modules/', views.ModuleList.as_view(), name="modules"),
    path('courses/<str:slug>/<int:pk>/modules/<int:id>', views.ContentList.as_view(), name="contents"),
]
