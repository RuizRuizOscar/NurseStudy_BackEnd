from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.
class TimeStamped(models.Model):    #TODO
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()

        self.updated_date = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class User(models.Model):   # TimeStamped #TODO #FIXME 
    """User"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    ### hash_pwd varchar,   #TODO #FIXME 
    user_type = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True) ### Checar ###   #TODO #FIXME 

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.user_name}"


class Answer(models.Model):
    """ Answers """
    right_answer = models.CharField(max_length=255)
    wrong_answers = ArrayField(
            models.CharField(max_length=255, blank=True, default=""),
            size=10,
        )    #TODO ARRAY
    
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True) ### Checar ###   #TODO #FIXME 

    def __str__(self):
        return f"{self.right_answer} {self.wrong_answers}"


class DataAcquisitionMethod(models.Model):
    """ Data Acquisition Methods (DAM) """
    method = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.method}"


class Methodology(models.Model):
    """ Assessment Methodologies """
    methodology = models.CharField(max_length=255)

    # Relations
    data_acquisition_method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.PROTECT, related_name="methodologies")

    def __str__(self):
        return f"{self.methodology}"


class Question(models.Model):
    """ Questions """
    question = models.CharField(max_length=255)
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])   # 1 Facil, 2 Medio, 3 Dificil
    question_type = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])    # 1 VF, 2 doble opcion 
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    # Relations
    methodology = models.ForeignKey(Methodology, on_delete=models.PROTECT, related_name="questions")
    answer = models.OneToOneField(Answer, on_delete=models.PROTECT, related_name="question")

    def __str__(self):
        return f"{self.question} {self.difficulty} {self.question_type}"


class Grades(models.Model):
    """ Grades """
    input_answer = models.IntegerField(validators=[MinValueValidator(0)])
    result = models.BooleanField()
    created_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    # Relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="grades")
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="grades")

    def __str__(self):
        return f"{self.input_answer} {self.result}"


class Progress(models.Model):
    """ User Progress """
    methodology_progress = models.IntegerField(validators=[MinValueValidator(0)],)

    # Relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="progresses")
    methodology = models.ForeignKey(Methodology, on_delete=models.PROTECT, related_name="progresses")

    def __str__(self):
        return f"{self.methodology_progress}"


#serves_hot_dogs = models.BooleanField(default=False)
# https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/     

    

