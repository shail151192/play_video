from django.shortcuts import render
from django.http import HttpResponse
from home.models import Video
from django.conf import settings
from home.forms import VideoForm
from django.conf import settings
import os


def home_page(request):

        videos = Video.objects.all()
        return render(request, 'home/home.html', {'data':videos})


def upload(request):
    if request.method == 'GET':
        form = VideoForm()
        context = {'form': form}
        return render(request, 'home/upload.html', context)

    if request.method == 'POST':
        form = VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        vs = Video.objects.filter()
        context = {'videos': vs}
        return render(request,'home/home.html', context)


def play(request, id):
    print id
    video = Video.objects.get(id=id)
    return render(request, 'home/play.html', {'v':video})