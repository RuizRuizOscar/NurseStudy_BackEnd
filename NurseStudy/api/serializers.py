from rest_framework import serializers
from .models import Answer, DataAcquisitionMethod, Grades, Methodology, Progress, Question #, User
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
        fields = "__all__"

# --------------------------------------------------------

# DataAcquisitionMethod
class DamsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAcquisitionMethod
        fields = ["id", "method"]

class DamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAcquisitionMethod
        fields = "__all__"

# --------------------------------------------------------

# Grades
class GradesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ["id", "input_answer", "result"]

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = [
            "input_answer",
            "result",
            "created_by",
            "created_date",
            # "user_id",
            # "question_id",
        ]

# --------------------------------------------------------

# Methodology
class MethodologiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Methodology
        fields = ["id", "methodology"]

class MethodologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Methodology
        fields = "__all__"

# --------------------------------------------------------

# Progress
class ProgressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ["id", "methodology_progress"]

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = "__all__"

# --------------------------------------------------------

# Question
class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question", "difficulty", "question_type"]

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

# --------------------------------------------------------

# User
class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "user_name"]

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

    def create(self, validate_data):
        print(validate_data)
        user = User.objects.create_user(**validate_data)
        return user

# --------------------------------------------------------