# import json
# from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Max
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
    permission_classes = [IsAuthenticated,]
    queryset = Answer.objects.all().order_by("created_by")
    serializer_class = AnswersListSerializer

class CreateAnswersAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

class RetrieveAnswersAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

class UpdateAnswersAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

class DestroyAnswersAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

# -----------------------------------------------------------

# DataAcquisitionMethods (DAM)
class ListDamsAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsListSerializer

class CreateDamsAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

class RetrieveDamsAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

class UpdateDamsAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

class DestroyDamsAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = DataAcquisitionMethod.objects.all()
    serializer_class = DamsSerializer

# -----------------------------------------------------------

# Grades
class ListGradesAPIView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated,]
    queryset = Grades.objects.all()
    serializer_class = GradesListSerializer

class CreateGradesAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

class RetrieveGradesAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

class UpdateGradesAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

class DestroyGradesAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

# -----------------------------------------------------------

# Methodology
class ListMethodologiesAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesListSerializer

class CreateMethodologiesAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

class RetrieveMethodologiesAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

class UpdateMethodologiesAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

class DestroyMethodologiesAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Methodology.objects.all()
    serializer_class = MethodologiesSerializer

# -----------------------------------------------------------

# Progress
class ListProgressAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Progress.objects.all()
    serializer_class = ProgressListSerializer

class CreateProgressAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class RetrieveProgressAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class UpdateProgressAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class DestroyProgressAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

# -----------------------------------------------------------

# Question
class ListQuestionsAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all().order_by("created_by")
    serializer_class = QuestionsListSerializer

class CreateQuestionsAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

class RetrieveQuestionsAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

class UpdateQuestionsAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

class DestroyQuestionsAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

# -----------------------------------------------------------

class RetrieveQuestionAnswerMethodologyAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionAnswerMethodologySerializer

class ListQuestionAnswerMethodologyAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all().order_by("difficulty")
    serializer_class = QuestionAnswerMethodologyListSerializer


# -----------------------------------------------------------

# User
class ListUsersAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UsersListSerializer

class CreateUsersAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = []

class RetrieveUsersAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UpdateUsersAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class DestroyUsersAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# -----------------------------------------------------------

class RetrieveMethodologyDifficultyAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    def get(self, *args, **kwargs):
        methodology_id = kwargs["pk"] #url
        methodology = get_object_or_404(Methodology, pk=methodology_id) # modelo, field por el que va a buscar
        result = Question.objects.filter(methodology_id=methodology_id).aggregate(Max('difficulty')) # methodology_id=methodology_id el primero es el campo a buscar, el segundo es el valor obtenido
        return Response(result)

# -----------------------------------------------------------

class ListQuestionsByMethAPIView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated,]
    def get(self, *args, **kwargs):
        methodology_id = kwargs["methodologyURL"]
        difficulty_level = kwargs["difficultyURL"]

        user_id=self.request._user.id
        # print(user_id)
    
        queryset = Question.objects.filter(methodology_id=methodology_id, difficulty=difficulty_level)
        # total_questions_meth_level = queryset.count()
        valid_questions = queryset.exclude(id__in=Grades.objects.filter(question_id__in=queryset.values_list("id", flat=True), user_id=user_id).values_list("question_id",flat=True))    
        print(type(valid_questions))
        # # print(queryset.count())
        # question_ids = queryset.values_list("id", flat=True)
        # # print(question_ids)
        # answered_questions = Grades.objects.filter(question_id__in=question_ids, user_id=user_id).values_list("question_id",flat=True)
        # # print(answered_questions)
        # valid_questions = queryset.exclude(id__in=answered_questions)
        # # print(valid_questions.values_list("id",flat=True))
        
        try:
            next_question=valid_questions.first()
        except:
            loquesea()
        
        response = {
            "id":next_question.id,
            "question":next_question.question,
            "question_type":next_question.question_type,
            "right_answer":next_question.answer.right_answer,
            "wrong_answers":next_question.answer.wrong_answers,
        }
        return Response(response)

        # for item in queryset:
        #     print(item) #= list(item['question'])

        # return HttpResponse(json.simplejson.dumps(queryset), mimetype="application/json")

        # methodology = get_object_or_404(Methodology, pk=methodology_id) # modelo, field por el que va a buscar
        # result = Question.objects.filter(methodology_id=methodology_id).filter(difficulty=difficulty_level) #.values()
        # print(result)
        
        # return JsonResponse({"Question": list(result.values('id', 'question', 'question_type', 'methodology', 'answer_id'))})
        
        
        # print(result[0].__dict__)
        # result2 = Answer.objects.filter(id=answer_id)
        # result2 = Answer.objects.values_list('right_answer', flat = True)
        # .filter(id= result.id )
        
        # x = []
        # for q in result:
        #     item_as_dict = {}
        #     item_as_dict['question_type'] = q.question_type
        #     item_as_dict['right_answer'] = q.right_answer
        #     item_as_dict['wrong_answers'] = q.wrong_answers
        #     x.append(item_as_dict)

        # print(x)


        # return JsonResponse({"Answer": list(result2.values('right_answer'))})  #, 'wrong_answers'
        # return JsonResponse({"Question": list(result)}) #.values('question', 'question_type', 'methodology', 'answer')

        # result_json = serializers.serialize('json', result)
        # return HttpResponse(result_json, content_type='application/json')

        # result_list = list(my_queryset.values('first_named_field', 'second_named_field'))
        # return HttpResponse(json.data(result))
# -----------------------------------------------------------

class RetrieveProgressByUserAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    def get(self, *args, **kwargs):
        user = kwargs["pk"]
        methodology = get_object_or_404(Methodology, pk=methodology_id) # modelo, field por el que va a buscar
        result = Question.objects.filter(methodology_id=methodology_id).aggregate(Max('difficulty')) # methodology_id=methodology_id el primero es el campo a buscar, el segundo es el valor obtenido
        result2 = Progress.objects.filter(user_id)
        return Response(result)