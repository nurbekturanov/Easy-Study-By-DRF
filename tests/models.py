from django.db import models


# class Subject(models.Model):
#     title = models.CharField(max_length=150)
#     slug = models.SlugField(max_length=150)

#     def __str__(self):
#         return self.title


# class Test(models.Model):
#     title = models.CharField(max_length=150)
#     slug= models.SlugField(max_length=150)
#     question = models.CharField(max_length=500)
#     answer1 = models.CharField(max_length=500)
#     answer2 = models.CharField(max_length=500)
#     answer3 = models.CharField(max_length=500)
#     answer4 = models.CharField(max_length=500)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests')

#     def __str__(self):
#         return self.question



from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=255)
    choices = models.TextField(blank=True)

    def __str__(self):
        return self.text[:30] + "..."

# class Answer(models.Model):
#     text = models.CharField(max_length=255)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     correct = models.BooleanField()

#     def __str__(self):
#         return self.text