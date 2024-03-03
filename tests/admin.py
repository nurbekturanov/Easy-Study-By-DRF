from django.contrib import admin

# from .models import Test, Subject
from .models import Question, Category


admin.site.register(Category)
# admin.site.register(Answer)

@admin.register(Question)
class TestAdmin(admin.ModelAdmin):
    list_display = ['text']