from django.shortcuts import render,redirect
from .utils import goofyapi
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'mainapp/home.html')
    else:
        return redirect('users/login_view')
    

def getHomedata(request):
    inst = goofyapi.Goofyapi()
    data = inst.get_homepage_sync()
    return JsonResponse(data)


def explore(request):
    if request.user.is_authenticated:
        return render(request,'mainapp/explore.html')
    else:
        return redirect('users/login_view')
    
def getExploredata(request):
    inst = goofyapi.Goofyapi()
    data = inst.get_explore_sync()
    return JsonResponse(data)