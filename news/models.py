from django.db import models
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news')

    class Meta:
        verbose_name_plural = "news"
