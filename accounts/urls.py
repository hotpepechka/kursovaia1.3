from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('PersonalArea/<int:pk>/', views.SongList.as_view(), name='PersonalArea'),

]