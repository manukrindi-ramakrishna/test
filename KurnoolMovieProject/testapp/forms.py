from django import forms
from testapp.models import Movie

class MovieModel(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'