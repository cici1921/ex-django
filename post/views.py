from django.shortcuts import render
from django.views.generic import ListView
from post.models import *

class PostLV(ListView):
    model = Post
    template_name = 'board.html'
    context_object_name = 'posts'
    paginate_by = 5
