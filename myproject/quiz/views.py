from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from result.models import Result
from question.models import Question, Answer
from .models import Quiz
from django.shortcuts import render

''' 
Why List view
1. get all the entry of the model assigned
2. do pagination for user
3. render using the existing template
4. handle get request
5. define context_object_name (quiz is pass in as to html)
    as quiz_list or object_list
'''
class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/main.html'

# class QuizDetailView(DetailView):
#     model = Quiz
#     template_name = 'quiz/quiz.html'
    

# since pk is passed in as require
# using pk to locate the specific quiz
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request,'quiz/quiz.html',{'obj': quiz})
    

# functin as view
# define the detail data view 
# the data_view(/quiz/<pk>/data) return a json obj 
# using js to fetch the data and render at quiz/<pk>
def quiz_detail_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for question in quiz.get_questions:
        answers = []
        for answer in question.get_answers:
            answers.append(answer.text)
        questions.append({question.text: answers})
    
    return JsonResponse({
        'data': questions,
        'time': quiz.time
    })
    