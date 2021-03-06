from django.http import Http404
from django.shortcuts import render
from music.models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    context = {'album': album}
    return render(request, 'music/details.html', context)
