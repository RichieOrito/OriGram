from multiprocessing import context
from re import template
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from posts.forms import PostForm

class createPostView(LoginRequiredMixin, CreateView):
    '''
    Create New Post View
    '''
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    context_object_name = 'form'

    def get_context_data(self, **kwargs: Any):
        '''
        Add user and profile to context.
        '''
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context

class PostFeedView(ListView):
    """
    Return all published posts.
    """
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 4
    context_object_name = 'posts'
