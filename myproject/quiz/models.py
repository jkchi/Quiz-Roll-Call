from django.db import models


# Quiz model
class Quiz(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField(
        default="This is a quiz",
        blank=True,
        null=True
    )

    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    number_of_questions = models.IntegerField()

    time = models.IntegerField(
        help_text="Duration of the quiz in minutes"
    )

    def __str__(self):
        '''
        display form in admin
        '''
        return f"{self.name}"


    @property
    def get_questions(self):
        # questions could be retrieved if the f key is binded
        # using related names it change the name of <lower_case_model_name>_set
        # to related name 
        
        # defination in question model
        # quiz = models.ForeignKey(
        #     Quiz,
        #     on_delete=models.CASCADE,
        #     related_name="questions",
        # )
        questions = list(self.questions.all())
        return questions