from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Posts

from django.urls import reverse_lazy


class PostListView(ListView):
    model = Posts
    template_name = 'post_list.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Posts 
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'login'
    model = Posts 
    fields = ['title', 'body',]
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'login'
    model = Posts 
    fields = ['title', 'body',]
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = 'login'
    model = Posts 
    fields = '__all__'
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('posts')