from django.contrib import admin
from filesystem.models import Folder, Topic, Document
# Register your models here.


class FolderAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(Folder, FolderAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(Topic, TopicAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "folder")
    list_filter = ("folder", "topics")
    list_display_links = ("id", "folder")


admin.site.register(Document, DocumentAdmin)
