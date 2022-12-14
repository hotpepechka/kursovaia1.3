from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from . import models
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import Song
from . models import Loved
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import NewSonger
from django.urls import reverse_lazy  # new


class MusicHome(TemplateView):
    template_name = 'index.html'




class AllSongList(ListView):
    model = Song
    template_name = 'AllSong.html'

    def get_queryset(self):
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            object_list = Song.objects.filter(genre__name__icontains=query)
            return object_list
        else:
            object_list = Song.objects.all()
            return object_list


def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)




class MusicDetail(DetailView):
    model = Song
    template_name = "MusicDetail.html"


class NewMusic(CreateView):
    model = Song
    form_class = NewSonger
    template_name = 'NewMusic.html'
    success_url = reverse_lazy("index")


class MusicDelete(DeleteView):
    model = Song
    template_name = 'deleteMusic.html'
    success_url = reverse_lazy('index')


class EditMusic(UpdateView):
    model = Song
    form_class = NewSonger
    template_name = 'editMusic.html'
    success_url = reverse_lazy('index')


class Meow(DetailView):
    model = models.Song
    template_name = 'SureToLove.html'
    def post(self, request, pk):
        models.Loved.objects.create(title=models.Song.objects.get(title=request.POST.get('title')), artist=models.Song.objects.get(artist=request.POST.get('artist')), user=request.user)
        instance = models.Song.objects.get(pk=pk)
        return HttpResponseRedirect(request.META.get('HTTP_ORIGIN') + f'/users/PersonalArea/{request.user.pk}/')

