from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Answer, DataAcquisitionMethod, Grades, Methodology, Progress, Question #, User 
from django.contrib.auth.models import User

from .serializers import AnswersListSerializer, AnswersSerializer
from .serializers import DamsListSerializer, DamsSerializer
from .serializers import GradesListSerializer, GradesSerializer
from .serializers import MethodologiesListSerializer, MethodologiesSerializer
from .serializers import ProgressListSerializer, ProgressSerializer
from .serializers import QuestionsListSerializer, QuestionsSerializer
from .serializers import UsersListSerializer, UsersSerializer

# Progress Logic goes here

# Create your views here.
# GET User.id & Token & username
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

# Answer
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

# DataAcquisitionMethods (DAM)
class ListDamsAPIView(generics.ListAPIView):
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsListSerializer

class CreateDamsAPIView(generics.CreateAPIView):
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

class RetrieveDamsAPIView(generics.RetrieveAPIView):
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

class UpdateDamsAPIView(generics.UpdateAPIView):
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

class DestroyDamsAPIView(generics.DestroyAPIView):
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

# -----------------------------------------------------------

# Grades
class ListGradesAPIView(generics.ListAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesListSerializer

class CreateGradesAPIView(generics.CreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

class RetrieveGradesAPIView(generics.RetrieveAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

class UpdateGradesAPIView(generics.UpdateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

class DestroyGradesAPIView(generics.DestroyAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

# -----------------------------------------------------------

# Methodology
class ListMethodologiesAPIView(generics.ListAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesListSerializer

class CreateMethodologiesAPIView(generics.CreateAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

class RetrieveMethodologiesAPIView(generics.RetrieveAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

class UpdateMethodologiesAPIView(generics.UpdateAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

class DestroyMethodologiesAPIView(generics.DestroyAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

# -----------------------------------------------------------

# Progress
class ListProgressAPIView(generics.ListAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressListSerializer

class CreateProgressAPIView(generics.CreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class RetrieveProgressAPIView(generics.RetrieveAPIView):
    queryset = Progress.objects.all()
    # print(queryset)
    serializer_class = ProgressSerializer

class UpdateProgressAPIView(generics.UpdateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class DestroyProgressAPIView(generics.DestroyAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

# -----------------------------------------------------------

# Question
class ListQuestionsAPIView(generics.ListAPIView):
    queryset = Question.objects.all().order_by("created_by")
    serializer_class = QuestionsListSerializer

class CreateQuestionsAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

class RetrieveQuestionsAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

class UpdateQuestionsAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

class DestroyQuestionsAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

# -----------------------------------------------------------

# User
class ListUsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer

class CreateUsersAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = []

class RetrieveUsersAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    
    # def sample_view(username):
    #     current_user = username.user
    #     print current_user.id

class UpdateUsersAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class DestroyUsersAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# -----------------------------------------------------------