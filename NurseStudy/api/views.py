from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from rest_framework import generics
from rest_framework import viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Answer, DataAcquisitionMethod, Grades, Methodology, Progress, Question
from django.contrib.auth.models import User

from .serializers import AnswersListSerializer, AnswersSerializer
from .serializers import DamsListSerializer, DamsSerializer
from .serializers import GradesListSerializer, GradesSerializer
from .serializers import MethodologiesListSerializer, MethodologiesSerializer
from .serializers import ProgressListSerializer, ProgressSerializer
from .serializers import QuestionsListSerializer, QuestionsSerializer
from .serializers import UsersListSerializer, UsersSerializer
from .serializers import QuestionAnswerMethodologySerializer, QuestionAnswerMethodologyListSerializer
from .serializers import MethodologyDifficultySerializer, QuestionsAnswersMethodologyDifficultySerializer

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

class RetrieveQuestionAnswerMethodologyAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionAnswerMethodologySerializer

class ListQuestionAnswerMethodologyAPIView(generics.ListAPIView):
    queryset = Question.objects.all().order_by("methodology")
    serializer_class = QuestionAnswerMethodologyListSerializer


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

class UpdateUsersAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class DestroyUsersAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# -----------------------------------------------------------

class RetrieveMethodologyDifficultyAPIView(generics.RetrieveAPIView):
    def get(self, *args, **kwargs):
        methodology_id = kwargs["pk"] #url
        methodology = get_object_or_404(Methodology, pk=methodology_id) # modelo, field por el que va a buscar
        result = Question.objects.filter(methodology_id=methodology_id).aggregate(Max('difficulty')) # methodology_id=methodology_id el primero es el campo a buscar, el segundo es el valor obtenido
        return Response(result)

# -----------------------------------------------------------

class ListQuestionsByMethAPIView(generics.ListAPIView):
    def get(self, *args, **kwargs):
        methodology_id= kwargs["methodologyURL"]
        difficulty_level= kwargs["difficultyURL"]
        user_id=self.request._user.id
    
        queryset= Question.objects.filter(methodology_id=methodology_id, difficulty=difficulty_level)
        question_ids= queryset.values_list("id", flat=True)
        answered_questions= Grades.objects.filter(question_id__in=question_ids, user_id=user_id)
        right_answered_questions= answered_questions.filter(result=True)

        remaining_questions= queryset.exclude(id__in=answered_questions.values_list("question_id",flat=True))

        next_question=remaining_questions.first()
        total_questions= queryset.count()
        questions_to_be_answered= int(total_questions*0.6)+1
        if next_question is None and right_answered_questions.count()<questions_to_be_answered:
            wrong_answered_questions= queryset.exclude(id__in=right_answered_questions.values_list("question_id",flat=True))
            next_wrong_question= wrong_answered_questions.first()
            response = {
                "id":next_wrong_question.id,
                "question":next_wrong_question.question,
                "question_type":next_wrong_question.question_type,
                "right_answer":next_wrong_question.answer.right_answer,
                "wrong_answers":next_wrong_question.answer.wrong_answers,
            }
            return Response(response) #regresa los valores de la pregunta actual
        
        if next_question is None and right_answered_questions.count()>=questions_to_be_answered:
            return Response({
                "is_ending":True
            })

        response = {
            "id":next_question.id,
            "question":next_question.question,
            "question_type":next_question.question_type,
            "right_answer":next_question.answer.right_answer,
            "wrong_answers":next_question.answer.wrong_answers,
        }
        return Response(response)

# -----------------------------------------------------------

class CreateUpdateGradesProgressArgsAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        print(self.__dict__)
        print(request.data)
        methodology_id = request.data["methodology_id"]
        result= request.data["result"]
        q_id= request.data["question_id"]
        user_id=self.request._user.id
        user_instance=self.request._user

        created_grade= Grades.objects.create(
            input_answer="0",   # No es requerido en este endpoint
            result=result,
            created_by=user_instance,
            created_date=timezone.now(),
            user=user_instance,
            question=Question.objects.get(id=q_id)
        )
                    
        if result == 1:
            p = Progress.objects.get(methodology_id=methodology_id, user_id=user_id)
            p.methodology_progress= p.methodology_progress+1
            p.save()

        return Response({
            "result":"ok"
        })        
    
# -----------------------------------------------------------

class RetrieveProgressByUserAPIView(generics.RetrieveAPIView):
    def get(self, *args, **kwargs):
        methodology_id = kwargs["methodologyURL"]
        user_id=self.request._user.id

        progress = Progress.objects.filter(methodology_id=methodology_id, user_id=user_id).first()
        if progress is not None:
            response = {
                "methodology_progress": progress.methodology_progress,
                "level": 1+progress.methodology_progress//6
            }
            return Response(response)
        
        return Response({
            "result":"Not found",
        })

# -----------------------------------------------------------

class CountQuestionsByMethAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        methodology_id= kwargs["methodologyURL"] #request.data["methodology_id"]
        difficulty_level= kwargs["difficultyURL"] #request.data["difficulty"]
    
        total_questions_meth_diff = Question.objects.filter(methodology_id=methodology_id, difficulty=difficulty_level).count()

        return Response({
            "total_questions_by_meth_by_diff":total_questions_meth_diff
        })