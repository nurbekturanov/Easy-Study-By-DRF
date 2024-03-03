from rest_framework import serializers

from .models import Course, CourseModule, Module, Content


class CourseSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # course_module = serializers.SlugField()
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'body', 'image', 'video', 'slug', 'created_at', 'author', 'course_module']


class CourseModuleSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer(many=True, read_only=True)
    courses = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = CourseModule
        fields = ['id', 'title', 'description', 'slug', 'courses']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'description', 'order']


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'module', 'title', 'author', 'image', 'file', 'video', 'body', 'order']