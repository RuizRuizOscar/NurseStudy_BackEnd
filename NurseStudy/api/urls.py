from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from django.conf.urls import url
from .views import CustomObtainAuthToken

from .views import ListAnswersAPIView, RetrieveAnswersAPIView, DestroyAnswersAPIView, UpdateAnswersAPIView, CreateAnswersAPIView
from .views import ListDamsAPIView, RetrieveDamsAPIView, DestroyDamsAPIView, UpdateDamsAPIView, CreateDamsAPIView
from .views import ListGradesAPIView, RetrieveGradesAPIView, DestroyGradesAPIView, UpdateGradesAPIView, CreateGradesAPIView
from .views import ListMethodologiesAPIView, RetrieveMethodologiesAPIView, DestroyMethodologiesAPIView, UpdateMethodologiesAPIView, CreateMethodologiesAPIView
from .views import ListProgressAPIView, RetrieveProgressAPIView, DestroyProgressAPIView, UpdateProgressAPIView, CreateProgressAPIView
from .views import ListQuestionsAPIView, RetrieveQuestionsAPIView, DestroyQuestionsAPIView, UpdateQuestionsAPIView, CreateQuestionsAPIView
from .views import ListUsersAPIView, RetrieveUsersAPIView, DestroyUsersAPIView, UpdateUsersAPIView, CreateUsersAPIView
from .views import RetrieveQuestionAnswerMethodologyAPIView, ListQuestionAnswerMethodologyAPIView

urlpatterns = [
    # URLs Answers
    path("answers/", ListAnswersAPIView.as_view(), name="list-answers"),
    path("answers/create/", CreateAnswersAPIView.as_view(), name="create-answers"),
    path("answers/<int:pk>/", RetrieveAnswersAPIView.as_view(), name="retrieve-answers"),
    path("answers/<int:pk>/update/", UpdateAnswersAPIView.as_view(), name="update-answers"),
    path("answers/<int:pk>/destroy/", DestroyAnswersAPIView.as_view(), name="destroy-answers"),

    # URLs DataAcquisitionMethods (DAMs)
    path("dams/", ListDamsAPIView.as_view(), name="list-dams"),
    path("dams/create/", CreateDamsAPIView.as_view(), name="create-dams"),
    path("dams/<int:pk>/", RetrieveDamsAPIView.as_view(), name="retrieve-dams"),
    path("dams/<int:pk>/update/", UpdateDamsAPIView.as_view(), name="update-dams"),
    path("dams/<int:pk>/destroy/", DestroyDamsAPIView.as_view(), name="destroy-dams"),

    # URLs Grades
    path("grades/", ListGradesAPIView.as_view(), name="list-grades"),
    path("grades/create/", CreateGradesAPIView.as_view(), name="create-grades"),
    path("grades/<int:pk>/", RetrieveGradesAPIView.as_view(), name="retrieve-grades"),
    path("grades/<int:pk>/update/", UpdateGradesAPIView.as_view(), name="update-grades"),
    path("grades/<int:pk>/destroy/", DestroyGradesAPIView.as_view(), name="destroy-grades"),

    # URLs Methodologies
    path("method/", ListMethodologiesAPIView.as_view(), name="list-methodologies"),
    path("method/create/", CreateMethodologiesAPIView.as_view(), name="create-methodologies"),
    path("method/<int:pk>/", RetrieveMethodologiesAPIView.as_view(), name="retrieve-methodologies"),
    path("method/<int:pk>/update/", UpdateMethodologiesAPIView.as_view(), name="update-methodologies"),
    path("method/<int:pk>/destroy/", DestroyMethodologiesAPIView.as_view(), name="destroy-methodologies"),

    # URLs Progress
    path("progress/", ListProgressAPIView.as_view(), name="list-progress"),
    path("progress/create/", CreateProgressAPIView.as_view(), name="create-progress"),
    path("progress/<int:pk>/", RetrieveProgressAPIView.as_view(), name="retrieve-progress"),
    path("progress/<int:pk>/update/", UpdateProgressAPIView.as_view(), name="update-progress"),
    path("progress/<int:pk>/destroy/", DestroyProgressAPIView.as_view(), name="destroy-progress"),

    # URLs Questions
    path("questions/", ListQuestionsAPIView.as_view(), name="list-questions"),
    path("questions/create/", CreateQuestionsAPIView.as_view(), name="create-questions"),
    path("questions/<int:pk>/", RetrieveQuestionsAPIView.as_view(), name="retrieve-questions"),
    path("questions/<int:pk>/update/", UpdateQuestionsAPIView.as_view(), name="update-questions"),
    path("questions/<int:pk>/destroy/", DestroyQuestionsAPIView.as_view(), name="destroy-questions"),

    # URLs Users
    path("users/", ListUsersAPIView.as_view(), name="list-users"),
    path("users/create/", CreateUsersAPIView.as_view(), name="create-users"),
    path("users/<int:pk>/", RetrieveUsersAPIView.as_view(), name="retrieve-users"),
    path("users/<int:pk>/update/", UpdateUsersAPIView.as_view(), name="update-users"),
    path("users/<int:pk>/destroy/", DestroyUsersAPIView.as_view(), name="destroy-users"),
    path("users/login/", obtain_auth_token, name="login-users"),

    # URLs Token Auth
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('token-id-username/', CustomObtainAuthToken.as_view(), name='token-id-username'),
    path('answ-ques/<int:pk>/', RetrieveQuestionAnswerMethodologyAPIView.as_view(), name='retrieve-question-answer-methodology'),
    path('answ-ques/', ListQuestionAnswerMethodologyAPIView.as_view(), name='list-questions-answers-methodologies'),
]