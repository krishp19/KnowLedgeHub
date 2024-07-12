from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserLogoutView(LogoutView):
    template_name = 'website/templates/home.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')