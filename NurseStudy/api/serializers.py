from rest_framework import serializers
from .models import Answer, DataAcquisitionMethod, Grades, Methodology, Question, Progress #, User  
from django.contrib.auth.models import User

#Serializers define the API representation

# Answers
class AnswersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "right_answer", "wrong_answers"]

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["right_answer", "wrong_answers"]

# --------------------------------------------------------

# DataAcquisitionMethod
class DamsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAcquisitionMethod
        fields = ["id", "method"]

class DamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAcquisitionMethod
        fields = ["method"]
# --------------------------------------------------------

# Grades
class GradesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ["id", "input_answer", "result"]

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ["input_answer", "result", "question"] #TODO user

    def evalua():
        if Grades.input_answer == True:
            Grades.result = True
        else:
            Grades.result = False


# --------------------------------------------------------

# Methodology
class MethodologiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Methodology
        fields = ["id", "methodology"]

class MethodologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Methodology
        fields = ["methodology", "data_acquisition_method"]

# --------------------------------------------------------

# Progress
class ProgressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ["methodology_progress"]

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ["methodology_progress", "methodology", "user"] #TODO user

# --------------------------------------------------------

# Question
class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question", "difficulty", "question_type"]

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question", "difficulty", "question_type", "methodology", "answer"]

# --------------------------------------------------------

# User
class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    # def create(self, validate_data): # NO HACE NADA!
    #     print(validate_data)
    #     user = User.objects.create_user(**validate_data)
    #     # progress =  Progress.objects.create( #TODO DELETE block
    #     #     methodology_progress='0',
    #     #     user_id='1',
    #     #     methodology_id='2')
    #     # # self.init_progress()
    #     return user

class QuestionAnswerMethodologyListSerializer(serializers.ModelSerializer):
    answer = AnswersListSerializer()
    methodology = MethodologiesListSerializer(many=False)

    class Meta:
        model = Question
        fields = [
            "id",
            "question",
            "difficulty",
            "question_type",
            "answer",
            "methodology",
        ]

class QuestionAnswerMethodologySerializer(serializers.ModelSerializer):
    answer = AnswersListSerializer()
    methodology = MethodologiesListSerializer(many=False)

    class Meta:
        model = Question
        fields = [
            "id",
            "question",
            "difficulty",
            "question_type",
            "answer",
            "methodology",
        ]

# Progress Logic goes here
    # def init_progress(self):
    #     progress =  Progress(
    #         methodology_progress='0',
    #         user='1',
    #         methodology='2'
    #     )
    #     progress.save()

# --------------------------------------------------------

class MethodologyDifficultySerializer(serializers.ModelSerializer):
    questions = MethodologiesListSerializer(many=True)
    class Meta:
        model = Question
        fields = ["id", "questions", "difficulty",]
        
        # max_rated_entry = YourModel.objects.latest()
        # return max_rated_entry.details