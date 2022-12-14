from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('<int:pk>/PersonalArea/', views.SongList.as_view(), name='PersonalArea'),
    path('<int:pk>/AllSongs/', views.AllSongList.as_view(), name='AllSong'),
    path('<int:pk>/Loved/', views.LovedList.as_view(), name='Loved'),
    path('NewSong/', views.NewMusic.as_view(), name='NewSong'),
    path('<int:pk>/DeleteSong/', views.MusicDelete.as_view(), name='DeleteSong'),
    path('<int:pk>/edit', views.EditMusic.as_view(), name='EditSong'),
    path('<int:pk>/', views.MusicDetail.as_view(), name='MusicDetail'),
    path('<int:pk>/ToLoved', views.LovedMusic.as_view(), name='SureToLove'),

]