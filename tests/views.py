from rest_framework import generics
# from .models import Test, Subject
# from .serializers import TestSerializer, SubjectSerializer
from .models import Category, Question
from .serializers import CategorySerializer, QuestionSerializer


# class SubjectList(generics.ListAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer


# class TestList(generics.ListAPIView):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer

#     def get_queryset(self):
#         slug = self.kwargs['slug']
#         return Test.objects.filter(subject__slug=slug)
        


# class TestDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Question.objects.filter(category__slug=slug)
    
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer