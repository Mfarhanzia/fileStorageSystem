from django.urls import path
from filesystem.views import home


urlpatterns = [
    path("", home, name="home"),
]

