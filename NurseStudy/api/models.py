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
    admin = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True) ### Checar ###   #TODO #FIXME 

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.user_name}"



class Template(models.Model):
    """ Templates de Preguntas """
    template = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.template}"
    

class Answer(models.Model):
    """ Answers """
    answer = models.CharField(max_length=255)
    # template_id = models.CharField(max_length=20)
    # question_id = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True) ### Checar ###   #TODO #FIXME 

    # Relations
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="answers")
    template = models.ForeignKey(Template, on_delete=models.PROTECT, related_name="answers")

    def __str__(self):
        return f"{self.answer} {self.template_id} {self.question_id}"

class DataAcquisitionMethod(models.Model):
    """ Método de Obtención de Datos (MOD) """
    method = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.metodo}"
    
class Methodology(models.Model):
    """ Tema de Valoración """
    methodology = models.CharField(max_length=255)

    # Relations
    data_acquisition_method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.PROTECT, related_name="methodologies")

    def __str__(self):
        return f"{self.methodology}"

class Question(models.Model):
    """ Questions """
    question = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    # right_answer_id = models.CharField(max_length=20) #TODO
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    # Relations
    template = models.ForeignKey(Template, on_delete=models.PROTECT, related_name="questions")
    methodology = models.ForeignKey(Methodology, on_delete=models.PROTECT, related_name="questions")
    right_answer = models.ForeignKey(Answer, on_delete=models.PROTECT, related_name="question") #TODO

    def __str__(self):
        return f"{self.question} {self.difficulty}"

class Grades(models.Model):
    """ Grades """
    input_answer = models.IntegerField(max_length=20)
    result = models.BooleanField()
    created_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    # Relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="grades")
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="grades")

    def __str__(self):
        return f"{self.user_id} {self.question_id} {self.result}"


#serves_hot_dogs = models.BooleanField(default=False)
# https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/     

    

