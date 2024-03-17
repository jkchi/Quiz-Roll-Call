from django.db import models
     
from quiz.models import Quiz
# auth user is implemented by django
from django.contrib.auth.models import User



class Result(models.Model):
    """
    get the result of a quiz of a user
    """ 
    
    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.DecimalField(
        # two digit of 100 scale
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    
    def __str__(self):
        return f"{str(self.pk)}"
