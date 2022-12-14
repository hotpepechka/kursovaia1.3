from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name="index"),
        path('<int:pk>/AllSongs/', views.AllSongList.as_view(), name='AllSong'),
    path('NewSong/', views.NewMusic.as_view(), name='NewSong'),
    path('<int:pk>/DeleteSong/', views.MusicDelete.as_view(), name='DeleteSong'),
    path('<int:pk>/edit', views.EditMusic.as_view(), name='EditSong'),
    path('<int:pk>/', views.MusicDetail.as_view(), name='MusicDetail'),
    path('product/<int:pk>/ToLoved', views.Meow.as_view(), name='SureToLove'),

]