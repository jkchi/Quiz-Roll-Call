from django.contrib import admin
from .models import Quiz

# register table quiz so it could be edited in admin site
admin.site.register(Quiz)
