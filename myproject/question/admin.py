from django.contrib import admin
from .models import Question
from .models import Answer

# register table Question,Answer so it could be edited in admin site
admin.site.register(Question)
admin.site.register(Answer)

