from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

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

# class User(models.Model):   # TimeStamped #TODO #FIXME 
#     """User"""

#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=20, unique=True)
#     #password varchar,   #TODO #FIXME 
#     user_type = models.CharField(max_length=20)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now_add=True) ### Checar ###   #TODO #FIXME 

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} {self.username}"

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# class UserDetails(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, 
#         related_name='userdetail_related')
    

class Answer(TimeStamped):
    """ Answers """
    right_answer = models.CharField(max_length=255)
    wrong_answers = ArrayField(
            models.CharField(max_length=255, blank=True, default=""),
            size=10,
        )
    
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.right_answer} {self.wrong_answers}"

class DataAcquisitionMethod(models.Model):
    """ Data Acquisition Methods (DAM) """
    DATA_ACQUISITION_METHODS =(
        ("OBSERVACION", "Observación"),
        ("ENTREVISTA", "Entrevista"),
        ("EXPLORACION", "Exploración Física"),
    )
    method = models.CharField(
        max_length=50,
        choices = DATA_ACQUISITION_METHODS,
        default="OBSERVACION",
    )
    
    def __str__(self):
        return f"{self.method}"

class Methodology(models.Model):
    """ Assessment Methodologies """
    METHODOLOGIES =(
        ("PATRONES", "Patrones funcionales"),
        ("CEFALOCAUDAL", "Cefalocaudal"),
        ("HABITOS", "Hábitos externos"),
        ("ANAMNESIS", "Anamnesis de enfermería"),
        ("PALPACION", "Palpación"),
        ("INSPECCION", "Inspección"),
    ) #https://docs.djangoproject.com/en/3.2/ref/models/fields/ ver human readable
    methodology = models.CharField(
        max_length=255,
        choices = METHODOLOGIES,
        default="CEFALOCAUDAL",
    )

    # Relations
    data_acquisition_method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.PROTECT, related_name="methodologies")

    def __str__(self):
        return f"{self.methodology}"

class Question(TimeStamped):
    """ Questions """
    question = models.CharField(max_length=255)
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])   # 1 Facil, 2 Medio, 3 Dificil
    question_type = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])    # 1 VF, 2 doble opcion 
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    # created_date = models.DateTimeField(auto_now_add=True)
    # updated_date = models.DateTimeField(auto_now_add=True)

    # Relations
    methodology = models.ForeignKey(Methodology, on_delete=models.PROTECT, related_name="questions")
    answer = models.OneToOneField(Answer, on_delete=models.PROTECT, related_name="question")

    def __str__(self):
        return f"{self.question} {self.difficulty} {self.question_type} {self.answer} {self.methodology}"

class Grades(models.Model):
    """ Grades """
    input_answer = models.CharField(max_length=255)
    result = models.BooleanField()
    created_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    # Relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="grades")
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="grades")

    def __str__(self):
        return f"{self.input_answer} {self.result} {self.question}"

class Progress(models.Model):
    """ User Progress """
    methodology_progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(18)],)

    # Relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="progresses")
    methodology = models.ForeignKey(Methodology, on_delete=models.PROTECT, related_name="progresses", null=True)

    def __str__(self):
        return f"{self.methodology_progress, self.user, self.methodology}"

    def level_up(self):
        self.methodology_progress += 1
        self.save()
        return self.methodology_progress