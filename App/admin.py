from django.contrib import admin
from . models import Song
from . models import Loved


admin.site.register(Song)
admin.site.register(Loved)
# Register your models here.
