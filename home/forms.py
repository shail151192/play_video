from django import forms
from home.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'video', 'thumbnail']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Video name'}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Select video'}))
    thumbnail = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload thumbnail'}))
