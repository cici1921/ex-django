from django.shortcuts import render
from django.views.generic import ListView

class PostLV(ListView):
    model = Post
    template_name = 'board.html'
    context_object_name = 'posts'
    paginate_by = 5
