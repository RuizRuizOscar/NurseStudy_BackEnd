from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Answer, DataAcquisitionMethod, Grades, Methodology, Progress, Question, User

from .serializers import AnswersListSerializer, AnswersSerializer

# Create your views here.

class ListAnswersAPIView(generics.ListAPIView):
    queryset = Answer.objects.all().order_by("created_by")
    serializer_class = AnswersListSerializer

class CreateAnswersAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

class RetrieveAnswersAPIView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

class UpdateAnswersAPIView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

class DestroyAnswersAPIView(generics.DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

# -----------------------------------------------------------