from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from result.models import Result
from question.models import Question, Answer
from .models import Quiz
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json


''' 
Why List view
1. get all the entry of the model assigned
2. do pagination for user
3. render using the existing template
4. handle get request
5. define context_object_name (quiz is pass in as to html)
    as quiz_list or object_list
'''


class QuizListView(LoginRequiredMixin,ListView):
    model = Quiz
    template_name = 'quiz/main.html'

# class QuizDetailView(DetailView):
#     model = Quiz
#     template_name = 'quiz/quiz.html'
    

# since pk is passed in as require
# using pk to locate the specific quiz
@login_required
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request,'quiz/quiz.html',{'object': quiz})
    

# functin as view
# define the detail data view 
# the data_view(/quiz/<pk>/data) return a json obj 
# using js to fetch the data and render at quiz/<pk>
# notice only the question text is passed as json
# the post request from the from can not use question id to match the question
# the text of each question has to be unique
@login_required
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


@login_required
def save_quiz_view(request, pk):
    # only respond to related header
    if request.accepts("application/json"):
        # get the POST data from request
        # using front end to avoid double post
        data = json.loads(request.body)

        # remove the csrf token from the post data
        questions = []

        for k in data.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / len(questions) 
        results = []

        for q in questions:
            a_selected = data[q.text]

            if a_selected != '':
                correct_answer = Answer.objects.filter(question=q).get(correct=True)
                if a_selected == correct_answer.text:
                    score += 1
                
                results.append({q.text: {
                    'correct_answer': correct_answer.text,
                    'answered': a_selected
                }})
            else:
                results.append({q.text: 'not answered'})

        final_score = score * multiplier


        Result.objects.create(quiz=quiz, user=user, score=final_score)

        json_response = {
            'score': final_score,
            'correct_questions': score,
            'results': results
        }  
    return JsonResponse(json_response)