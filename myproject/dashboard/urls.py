from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    # define the user dashboard page, name is dashboard
    # the name is used to redirect
    path('', views.MainView.as_view(), name='main'),
    # the logout rediect is define in settings.py
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]