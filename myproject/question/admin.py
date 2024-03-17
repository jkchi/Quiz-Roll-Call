from django.contrib import admin
from .models import Question
from .models import Answer


# create display of answer in a line form
class AnswerInline(admin.TabularInline):
    model = Answer

# allow edit answer in question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

# register the new edit in Question 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

