from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import MusicForm


def list_albums(request):
    albums = Album.objects.all()
    return render(request, "music/list_albums.html",
                  {"albums": albums})

def single_album(request, pk):
    pass

def add_album(request):
    if request.method == 'GET':
        form = MusicForm()
    else:
        form = MusicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "music/new.html", {"form": form})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = MusicForm(instance=album)
    else:
        form = MusicForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to="list_albums")
    return render(request, "music/edit.html", {
        "form": form, "album": album
    })

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "music/delete.html",
                  {"album": album})

def details_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "music/details.html",
                  {"album": album})