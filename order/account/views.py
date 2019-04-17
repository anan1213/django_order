from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from .forms import LoginForm

class ProfileView(generic.TemplateView):
    template_name = 'account/profile.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'account/logout.html'
