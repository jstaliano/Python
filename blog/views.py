from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
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

class BlogCreateView(SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    #context_object_name = 'custom'
    fields = ('autor','titulo','conteudo')
    success_message = 'Criado Postagem Título:"%(field)s" com Sucesso'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogUpdateView(SuccessMessageMixin,UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    #context_object_name = 'custom'
    fields = ('titulo','conteudo')
    success_message = 'Postagem Título:"%(field)s" Alterado com Sucesso'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogDeleteView(SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    #context_object_name = 'custom'
    success_url = reverse_lazy('home')
    success_message = 'Postagem  excluída com Sucesso'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)



    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


