from django.contrib import admin
from . models import Song
from . models import Loved
from . models import Genre

admin.site.register(Song)
admin.site.register(Loved)
admin.site.register(Genre)
# Register your models here.
