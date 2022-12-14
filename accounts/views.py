from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from . models import MEOW
from django.views.generic import ListView, DetailView



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class SongList(ListView):
    model = MEOW
    template_name = 'personal_area.html'


