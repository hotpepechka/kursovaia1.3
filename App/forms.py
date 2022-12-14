from .models import Song
from django.forms import ModelForm, forms, TextInput
from .models import Loved


class NewSonger(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

class NewNewSonger(ModelForm):
    class Meta:
        model = Song
        fields = ("title", "artist")




