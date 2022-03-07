from django import forms
from .models import Album


class MusicForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
        ]
