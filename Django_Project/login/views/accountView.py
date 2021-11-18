from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
     get_user_model, logout as auth_logout,)
from django.contrib.auth.views import PasswordChangeView
from login.forms import MyPasswordChangeForm
from login.forms import UserCreateForm

User = get_user_model()

def Login(request):
    return render(request,'registration/login.html')

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChange(PasswordChangeView):
     form_class = MyPasswordChangeForm
     success_url = reverse_lazy('registration/password_reset_done')
     templatename = 'registration/password_reset_form.html'