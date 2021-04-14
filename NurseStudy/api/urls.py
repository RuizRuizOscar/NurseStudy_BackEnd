from django.urls import path, include

from .views import ListAnswersAPIView, RetrieveAnswersAPIView, DestroyAnswersAPIView, UpdateAnswersAPIView, CreateAnswersAPIView

urlpatterns = [
    path("answers/", ListAnswersAPIView.as_view(), name="list-answers"),
    path("answers/create/", CreateAnswersAPIView.as_view(), name="create-answers"),
    path("answers/<int:pk>/", RetrieveAnswersAPIView.as_view(), name="retrieve-answers"),
    path("answers/<int:pk>/update/", UpdateAnswersAPIView.as_view(), name="update-answers"),
    path("answers/<int:pk>/destroy/", DestroyAnswersAPIView.as_view(), name="destroy-answers"),
]