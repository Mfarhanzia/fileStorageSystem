from django.db import models
from django.core.validators import RegexValidator
from filesystem.helpers import document_upload_path

# Create your models here.

TITLE_REGEX = RegexValidator(
    r'^[a-zA-Zа-яА-Я0-9_!]+$', 'Enter valid Title.'
)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Folder(TimeStampedModel):
    """
    saves the Folder name
    """
    title = models.CharField(max_length=30, unique=True, validators=[TITLE_REGEX])

    def __str__(self):
        return "{}-{}".format(self.id, self.title)


class Topic(TimeStampedModel):
    """
    saves the Topic
    """
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "{}-{}".format(self.id, self.title)


class Document(TimeStampedModel):
    """
    saves the actual uploaded document
    """
    folder = models.ForeignKey(
        Folder, on_delete=models.SET_NULL, related_name="document_folder", null=True, blank=True
    )
    topics = models.ManyToManyField(Topic, related_name="document_topics")
    file = models.FileField(upload_to=document_upload_path, max_length=256)

    def __str__(self):
        return "{}".format(self.id)
