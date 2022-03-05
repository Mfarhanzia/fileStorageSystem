from rest_framework import serializers
from filesystem.models import Folder, Topic, Document
from filesystem.constants import MAX_UPLOAD_FILE_SIZE


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    filetype = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ('id', 'folder', 'topics', 'file', 'size', 'name', 'filetype', 'created_at')

        extra_kwargs = {
            "folder": {"required": True}
        }

    def get_size(self, instance):
        file_size = ''
        if instance.file and hasattr(instance.file, 'size'):
            file_size = instance.file.size
        return file_size

    def get_name(self, instance):
        file_name = ''
        if instance.file and hasattr(instance.file, 'name'):
            file_name = instance.file.name.split("--", 1)[-1]
        return file_name

    def get_filetype(self, instance):
        filename = instance.file.name
        return filename.split('.')[-1]

    def validate_file(self, file):
        if file.size > MAX_UPLOAD_FILE_SIZE:
            raise serializers.ValidationError("File size too big!")
        return file
