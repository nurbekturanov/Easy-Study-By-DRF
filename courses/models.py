from django.db import models
from django.conf import settings
from .fields import OrderField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from embed_video.fields import EmbedVideoField

class CourseModule(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='videos', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_created')
    course_module = models.ForeignKey(CourseModule, related_name='courses', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contents', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='content_images', blank=True, null=True)
    file = models.ImageField(upload_to='content_files', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    body = models.TextField()
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title