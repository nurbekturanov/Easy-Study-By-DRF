from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from courses.permissions import IsaAuthorOrReadOnly


class NewsList(generics.ListCreateAPIView):
    permission_classes = (IsaAuthorOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsaAuthorOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_object(self):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj