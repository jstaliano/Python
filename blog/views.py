from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from . models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #context_object_name = 'custom'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    #context_object_name = 'custom'
    fields = ('autor','slug','titulo','conteudo')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    #context_object_name = 'custom'
    fields = ('titulo','conteudo')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    #context_object_name = 'custom'
    success_url = reverse_lazy('home')


