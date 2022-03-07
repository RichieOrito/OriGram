from re import template
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User
from users.forms import SignupForm
from posts.models import Post
from users.models import Profile

class SignupView(FormView):
    """
    Signup View
    """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')