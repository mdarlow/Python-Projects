from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('CreateNewAccount/', views.CreateNewAccount, name="CreateNewAccount"),
]
