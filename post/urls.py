from django.contrib import admin
from django.urls import path
from post.views import *

app_name = 'post'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
]
