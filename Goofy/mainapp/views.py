from django.shortcuts import render,redirect
from .utils import goofyapi
from django.http import JsonResponse,HttpResponseForbidden,FileResponse,HttpRequest
from .models import LikedSong,Playlist
import os


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'mainapp/home.html')
    else:
        return redirect('login_view')
    

def getHomedata(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.get_homepage_sync()
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 


def explore(request):
    if request.user.is_authenticated:
        return render(request,'mainapp/explore.html')
    
    return redirect('login_view')

def likes(request):
    if request.user.is_authenticated:
        likedsongs = LikedSong.objects.filter(user=request.user).order_by('-liked_at')
        liked_songs_list = list(likedsongs.values_list('song_id',flat=True))
        inst = goofyapi.Goofyapi()
        data = inst.getSongdetails(liked_songs_list)
        return render(request,'mainapp/likes.html',context=data)
    
    return redirect('login_view')

def library(request):
    if request.user.is_authenticated:
        
        return render(request,'mainapp/library.html')
    
    return redirect('login_view')
    
def getExploredata(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.get_explore_sync()
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 


def getSuggestions(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.get_suggestions(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def createFileResponse(request,songId=None):
    if request:
        songId = request.GET.get("query")
    file_path = f'mainapp/static/mainapp/player/songs/{songId}.m4a'
    file_name = os.path.basename(file_path)
    response = FileResponse(open(file_path, 'rb'), content_type='audio/mp4')
    response['Content-Disposition'] = f'inline; filename="{file_name}"'
    response['Accept-Ranges'] = 'bytes'
    return response

def getSong(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        q = request.GET.getlist('query[]')
        inst.getMusic(q)
        return createFileResponse(None,q[0])
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getSearch(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getSearch(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getPlaylist(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getPlaylist(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getAlbum(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getAlbum(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getArtist(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getArtist(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getMoodpl(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getMoodpl(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 


def getRelated(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getRelated(request.GET.get('query'))
        inst.getMusic([i['videoId'] for i in data['related']])
        for song in data["related"]:
            if song["videoId"]+".m4a" not in os.listdir("mainapp/static/mainapp/player/songs/"):
                data['related'].remove(song)
           
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def like_song(request):
    if request.method == "POST" and request.user.is_authenticated:
        liked_song, created = LikedSong.objects.get_or_create(user=request.user, song_id=request.POST.get('query'))
        if created:
            return JsonResponse({'status': 'liked'})
        return JsonResponse({'status': 'already liked'})


def unlike_song(request):
    if request.method == "POST" and request.user.is_authenticated:
        liked_song = LikedSong.objects.filter(user=request.user, song_id=request.POST.get('query')).first()
        if liked_song:
            liked_song.delete()
            return JsonResponse({'status': 'unliked'})
        return JsonResponse({'status': 'not liked'})
    return JsonResponse({'status': 'error'}, status=400)


def getLikedSongs(request:HttpRequest):
    if request.method == "GET" and request.user.is_authenticated:
        likedsongs = LikedSong.objects.filter(user=request.user)
        liked_songs_list = list(likedsongs.values_list('song_id',flat=True))
        return JsonResponse({'likedsongs': liked_songs_list})


def getPlaylists(request:HttpRequest):
    if request.method == "GET" and request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user)
        playlists_data = [{
            'name': playlist.name,
            'description': playlist.description,
            'song_ids': playlist.song_ids,
            'playlist_id':playlist.playlist_id,
            'created_at': playlist.created_at,
            'updated_at': playlist.updated_at,
        } for playlist in playlists]
        return JsonResponse({'playlists': playlists_data})


def createPlaylist(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')

        if name:
            Playlist.objects.create(
                user=request.user,
                name=name,
                description=description
            )
            return redirect('library')