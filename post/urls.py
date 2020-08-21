from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
]
