from django.contrib import admin
from .models import Quiz
from question.models import Question
from question.models import Answer

# register table quiz so it could be edited in admin site


# create display of answer in a line form
class QuestionInline(admin.TabularInline):
    model = Question


# allow edit answer in question
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Quiz,QuizAdmin)
# register the new edit in Question 
