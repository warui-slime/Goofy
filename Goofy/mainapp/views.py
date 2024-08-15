from django.shortcuts import render,redirect,get_object_or_404
from .utils import goofyapi
from django.http import JsonResponse,HttpResponseForbidden,FileResponse,HttpRequest
from .models import LikedSong,Playlist,Image
from django.core.exceptions import ValidationError


import os


# Create your views here.

def index(request:HttpRequest):
    if request.user.is_authenticated:
        return render(request,'mainapp/base.html')
    else:
        return redirect('login_view')
def home(request):
    if request.user.is_authenticated:
        return render(request,'mainapp/home.html')
    else:
        return redirect('login_view')
    

def getHomedata(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.get_homepage_sync()
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 


def explore(request:HttpRequest):
    if request.user.is_authenticated:
        return render(request,'mainapp/explore.html')
    
    return redirect('login_view')

def likes(request:HttpRequest):
    if request.user.is_authenticated:
        return render(request,'mainapp/likes.html')
    
    return redirect('login_view')

def library(request:HttpRequest):
    if request.user.is_authenticated:
        
        return render(request,'mainapp/library.html')
    
    return redirect('login_view')

def profile(request:HttpRequest):
    if request.user.is_authenticated:
        return render(request,"mainapp/profile.html")

def getExploredata(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.get_explore_sync()
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 


def getSuggestions(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.get_suggestions(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def createFileResponse(request:HttpRequest,songId=None):
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

def clearSongs(request:HttpRequest):
    if request.user.is_authenticated:
        for file in os.listdir("mainapp/static/mainapp/player/songs/"):
            os.remove(os.path.join("mainapp/static/mainapp/player/songs/",file))
    return JsonResponse({})

def getSearch(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getSearch(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getPlaylist(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getPlaylist(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getAlbum(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getAlbum(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getArtist(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getArtist(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def getMoodpl(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getMoodpl(request.GET.get('query'))
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 


def getRelated(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        data = inst.getRelated(request.GET.get('query'))
        inst.getMusic([i['videoId'] for i in data['related'][0:3]])
        for song in data["related"][0:3]:
            if song["videoId"]+".m4a" not in os.listdir("mainapp/static/mainapp/player/songs/"):
                data['related'].remove(song)
           
        return JsonResponse(data)
    return HttpResponseForbidden("You do not have permission to access this page.") 

def like_song(request:HttpRequest):
    if request.method == "POST" and request.user.is_authenticated:
        liked_song, created = LikedSong.objects.get_or_create(user=request.user, song_id=request.POST.get('query'))
        if created:
            return JsonResponse({'status': 'liked'})
        return JsonResponse({'status': 'already liked'})


def unlike_song(request:HttpRequest):
    if request.method == "POST" and request.user.is_authenticated:
        liked_song = LikedSong.objects.filter(user=request.user, song_id=request.POST.get('query')).first()
        if liked_song:
            liked_song.delete()
            return JsonResponse({'status': 'unliked'})
        return JsonResponse({'status': 'not liked'})
    return JsonResponse({'status': 'error'}, status=400)


def getLikedSongs(request:HttpRequest):
    if request.method == "GET" and request.user.is_authenticated:
        likedsongs = LikedSong.objects.filter(user=request.user).order_by('-liked_at')
        liked_songs_list = list(likedsongs.values_list('song_id',flat=True))
        if liked_songs_list:
            inst = goofyapi.Goofyapi()
            data = inst.getSongdetails(liked_songs_list)
            return JsonResponse(data)
        return JsonResponse({"likedata":None})

def getLikedata(request:HttpRequest):
    if request.method == "GET" and request.user.is_authenticated:
        liked_songs = LikedSong.objects.filter(user=request.user).values_list('song_id', flat=True)
        if liked_songs:
            return JsonResponse({"likedids":list(liked_songs)})
        return JsonResponse({"likedids":[]})

def getPlaylists(request: HttpRequest):
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user).order_by('-created_at')
        playlists_data = [{
            'name': playlist.name,
            'description': playlist.description,
            'song_ids': playlist.song_ids,
            'playlist_id': playlist.playlist_id,
            'created_at': playlist.created_at,
            'updated_at': playlist.updated_at,
        } for playlist in playlists]
        return JsonResponse({'playlists': playlists_data})
    return JsonResponse({'error': 'Unauthorized'}, status=401)


def createPlaylist(request: HttpRequest):
    if request.user.is_authenticated:
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        song_id = request.POST.get('songId')  # Handling song_ids if needed
        
        if song_id:
            song_id= [song_id]
        else:
            song_id=[]
       
        
        if name:
            try:
                Playlist.objects.create(
                    user=request.user,
                    name=name,
                    description=description,
                    song_ids=song_id  # Include song_ids if applicable
                )
                return JsonResponse({'success':"OK"})
            except ValidationError as e:
                return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'error': 'Name is required'}, status=400)
    return JsonResponse({'error': 'Unauthorized'}, status=401)


def updatePlaylist(request:HttpRequest):
    if request.user.is_authenticated:
        playlist = get_object_or_404(Playlist, playlist_id=request.POST.get("playlist_id"), user=request.user)

        name = request.POST.get('name',playlist.name)
        description = request.POST.get('description', '')
        new_song_id = request.POST.get('song_id')  # Default to existing song_ids if not provided
        is_delete = request.POST.get("is_delete")

        if name:
            playlist.name = name
        if description:
            playlist.description = description

        if new_song_id and is_delete:
            songIds = playlist.song_ids.copy()
            songIds.remove(new_song_id)
            playlist.song_ids = songIds
        
        elif new_song_id:
            # Append new song IDs to the existing ones, ensuring no duplicates
            playlist.song_ids = list(set(playlist.song_ids + [new_song_id]))
       
        try:
            playlist.clean()  # Validate the data
            playlist.save()  # Save the updated playlist
            if new_song_id:
                return JsonResponse({'message': 'Playlist updated successfully'})
            else:
                return redirect("library")
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Unauthorized'}, status=401)


def deletePlaylist(request:HttpRequest):
    if request.user.is_authenticated and request.method=="POST":
        playlist = get_object_or_404(Playlist, playlist_id=request.POST.get("playlist_id"), user=request.user)
        playlist.delete()
        return redirect('library')


def getPlaylistData(request: HttpRequest):
    if request.user.is_authenticated and request.method=="GET":
        playlist = get_object_or_404(Playlist, playlist_id=request.GET.get("playlist_id"), user=request.user)
        inst = goofyapi.Goofyapi()
        pldata = inst.getSongdetails(playlist.song_ids)
      
        playlists_data = {
            'name': playlist.name,
            'description': playlist.description,
            'song_details': pldata,
            'playlist_id': playlist.playlist_id,
            'created_at': playlist.created_at,
            'updated_at': playlist.updated_at,
        } 
        return JsonResponse({'playlist': playlists_data})
    return JsonResponse({'error': 'Unauthorized'}, status=401)


def getLyrics(request:HttpRequest):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        songId = request.GET.get("songId")
        return JsonResponse({"lyrics":inst.getLyrics(songId)['lyrics']})
    

def getProfileImage(request:HttpRequest):
    if request.user.is_authenticated:
        try:
            image = Image.objects.get(user=request.user)
            return JsonResponse({"image":image.image})
        except Image.DoesNotExist:
            return JsonResponse({'error': "ERROR!"}, status=404)


def updateProfileImage(request:HttpRequest):
    if request.user.is_authenticated:
        Image.objects.update_or_create(
                    user=request.user,
                    defaults={
                    'image':request.POST.get("path"),
                    }
                )
        return JsonResponse({'success': "success"})
    return JsonResponse({'error': "ERROR!"}, status=400)