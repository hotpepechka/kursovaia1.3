from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from django.shortcuts import render, redirect
# imported our models
from django.core.paginator import Paginator
from . models import Song
from . models import Loved
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView




class MusicHome(TemplateView):
    template_name = 'index.html'



class SongList(ListView):
    model = Song
    template_name = 'personal_area.html'

class LovedList(ListView):
    model = Song
    template_name = 'Loved.html'

class AllSongList(ListView):
    model = Song
    template_name = 'AllSong.html'

def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)



def index1(request, pk):
    users = Loved.objects.filter(user=request.user.id).all()
    return render(request, "Loved.html", {"users": users})

class ButtonLoved(ListView):
    model = models.Loved
    template_name = 'SureToLove.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





