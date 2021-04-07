from django.db import models
from django.utils import timezone


# Create your models here.
class TimeStamped(models.Model):
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()

        self.updated_date = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class User(models.Model):   # ,TimeStamped #TODO #FIXME 
    """User"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    ### hash_pwd varchar,   #TODO #FIXME 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True) ### Checar ###   #TODO #FIXME 

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.user_name}"


class Answer(models.Model):
    """ Answers """
    answer = models.CharField(max_length=255)
    template_id = models.CharField(max_length=20)
    question_id = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True) ### Checar ###   #TODO #FIXME 

    def __str__(self):
        return f"{self.answer} {self.template_id} {self.question_id}"


class Grades(models.Model):
    """ Grades """
    user_id = models.CharField(max_length=20)
    question_id = models.CharField(max_length=20)
    input_answer = models.CharField(max_length=20)
    result = models.BooleanField()
    created_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} {self.question_id} {self.result}"


class Template(models.Model):
    """ Templates de Preguntas """
    template = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.template}"
    

class MetodoObtencionDatos(models.Model):
    """ Método de Obtención de Datos (MOD) """
    metodo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.metodo}"
    

class TemaValoracion(models.Model):
    """ Tema de Valoración """
    TemaValoracion = models.CharField(max_length=255)
    metodoObtencionDatos_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.TemaValoracion}"
    

class Question(models.Model):
    """ Questions """
    question = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    right_answer_id = models.CharField(max_length=20)
    template_id = models.CharField(max_length=20)
    metodoObtencionDatos_id = models.CharField(max_length=20)
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question} {self.difficulty}" 
    

