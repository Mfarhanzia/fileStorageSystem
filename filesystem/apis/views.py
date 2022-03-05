from rest_framework import generics, response, status
from filesystem.apis.serializers import FolderSerializer, TopicSerializer, DocumentSerializer
from filesystem.models import Folder, Topic, Document


class ListCreateFolders(generics.ListCreateAPIView):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()


class ListCreateTopics(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class ListCreateDocument(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        filters = {}
        if self.request.query_params.get("folder_id"):
            filters["folder_id"] = self.request.query_params.get("folder_id")
        if self.request.query_params.get("topics[]"):
            filters["topics__in"] = self.request.query_params.getlist("topics[]")
        return Document.objects.filter(**filters).distinct()
