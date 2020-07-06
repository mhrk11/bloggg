from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

class HomePageView(ListView):
    model=BlogPost
    template_name='home.html'
    context_object_name='blogs_list'


class BlogPageView(DetailView):
    model=BlogPost
    template_name='post_detail.html'


class BlogCreateView(CreateView):
    model=BlogPost
    template_name='post_new.html'
    fields=['title', 'author', 'body']


