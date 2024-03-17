from django.shortcuts import render, redirect
from django.urls import reverse
# HomeView inherent from Django view
from django.views import View

# Home page only serve as the redirect page 
# Home inherent request to handle the response
# If user not logged in redirect to login page
# If logged in redirect to user homepage(to be done)
class HomeView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))  
        # using namespace to point to the dashboard:dashboard
        return redirect(reverse('dashboard:main'))
