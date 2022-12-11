from .models import Song
from django.forms import ModelForm


class NewSonger(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'