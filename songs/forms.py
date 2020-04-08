from django import forms
from .models import Song,Artist,Rating

class SongForm(forms.ModelForm):
    Name = forms.CharField()
    Date_of_Release = forms.CharField()
    artist = forms.CharField()
    rating = forms.IntegerField()
    class Meta:
        model= Song
        fields= ['Name','Date_of_Release','artist','rating']

class RatingForm(forms.ModelForm):
    rating=forms.TextInput()

    class Meta:
        model= Rating
        fields =['rating']

class ArtistForm(forms.ModelForm):
    artist = forms.CharField()
    DOB = forms.CharField()
    Bio = forms.CharField()

    class Meta:
        model=Artist
        fields=['artist','DOB','Bio']