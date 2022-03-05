from django.urls import path
from .views import ListCreateFolders, ListCreateTopics, ListCreateDocument


urlpatterns = [
    path("folders", ListCreateFolders.as_view()),
    path("topics", ListCreateTopics.as_view()),
    path("documents", ListCreateDocument.as_view()),
]
