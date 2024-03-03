from rest_framework import serializers
# from .models import Subject, Test
from .models import Category, Question


# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = '__all__'
    

# class TestSerializer(serializers.ModelSerializer):
#     subject = SubjectSerializer(read_only=True)
#     class Meta:
#         model = Test
#         fields = ('id', 'title', 'question', 'answer1', 'answer2', 'answer3', 'answer4', 'subject')

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ('id', 'text', 'correct')

class QuestionSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True, read_only=True)
    category = CategorySerializer()
    choices = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'text', 'category', 'correct_answer', 'choices')
    
    def get_choices(self, obj):
        return obj.choices.split(';')
