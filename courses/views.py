from django.shortcuts import render
from rest_framework import generics
from .models import Course, CourseModule, Module, Content
from .serializers import CourseSerializer, CourseModuleSerializer, ModuleSerializer, ContentSerializer
from .permissions import IsaAuthorOrReadOnly, IsTeacherOrReadOnly


class CourseModuleList(generics.ListAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer


class CourseModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer


class CourseList(generics.ListCreateAPIView):
    permission_classes = (IsaAuthorOrReadOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Course.objects.filter(course_module__slug=slug)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsaAuthorOrReadOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class ModuleList(generics.ListCreateAPIView):
    permission_classes = (IsTeacherOrReadOnly,)
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return Module.objects.filter(course__id=id)
    
class ContentList(generics.ListCreateAPIView):
    permission_classes = (IsTeacherOrReadOnly,)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Content.objects.filter(module__id=id)
    

class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTeacherOrReadOnly,)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def content(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)