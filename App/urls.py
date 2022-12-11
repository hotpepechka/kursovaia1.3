from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('PersonalArea/', views.SongList.as_view(), name='PersonalArea'),
    path('<int:pk>/AllSongs/', views.AllSongList.as_view(), name='AllSong'),
    path('<int:pk>/Loved/', views.index1, name='Loved'),
    path('<int:pk>/ToLoved', views.ButtonLoved.as_view(), name='SureToLove'),
]