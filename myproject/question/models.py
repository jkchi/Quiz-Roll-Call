from django.db import models

# import quiz to be the fkey for model
from quiz.models import Quiz

# Create your models here.
class Question(models.Model):
    """
    Quesiton of a quiz
    """
    
    text = models.TextField()
    
    # bound a question to a quiz using pk
    # the related_name a
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    
    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Display form in admin
        """
        return f"{self.pk} - {str(self.text)}"

    @property
    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    """
    Answer of a quesiton
    """
  
    text = models.TextField()
    
    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    correct = models.BooleanField(default=False)
 
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    def __str__(self):
        return f"Question: {str(self.question.text)}, Ans: {str(self.text)}, Correct: {self.correct}"
    