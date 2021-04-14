from rest_framework import serializers
from .models import Answer, DataAcquisitionMethod, Grades, Methodology, Progress, Question, User

#Serializers define the API representation

class AnswersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "right_answer", "wrong_answers"]

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

# --------------------------------------------------------