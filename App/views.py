from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from django.shortcuts import render, redirect
# imported our models
from django.core.paginator import Paginator
from . models import Song
from django.views.generic import TemplateView




class MusicHome(TemplateView):
    template_name = 'index.html'


def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)