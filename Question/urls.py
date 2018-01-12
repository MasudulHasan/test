from django.conf.urls import url
from django.contrib import admin

from .views import add_question
urlpatterns = [
    url(r'^add/$', add_question, name="add_question"),
]
