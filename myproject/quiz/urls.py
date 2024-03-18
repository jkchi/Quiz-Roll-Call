from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'quiz'
urlpatterns = [
    path('', views.QuizListView.as_view(), name='main_view'),
    
    # notice register a function not a function call
    path('<pk>', views.quiz_view, name='quiz_view'),
    path('<pk>/data', views.quiz_detail_data_view, name='quiz_data_view'),
]