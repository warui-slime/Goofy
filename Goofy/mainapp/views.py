from django.shortcuts import render,redirect
from .utils import goofyapi
from django.http import JsonResponse,HttpResponseForbidden,FileResponse
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
        return render(request,'mainapp/likes.html')
    
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

def getSong(request):
    if request.user.is_authenticated:
        inst = goofyapi.Goofyapi()
        q = request.GET.get('query')
        inst.getMusic(q)
        # return JsonResponse({'ok':'fine'})
        file_path = 'mainapp/static/mainapp/player/song.m4a'
        file_name = os.path.basename(file_path)
        response = FileResponse(open(file_path, 'rb'), content_type='audio/mp4')
        response['Content-Disposition'] = f'inline; filename="{file_name}"'
        response['Accept-Ranges'] = 'bytes'
        return response
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