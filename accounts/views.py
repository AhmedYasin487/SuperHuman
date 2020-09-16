from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"
