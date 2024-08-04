from django.contrib import admin
from .models import LikedSong,Playlist
# Register your models here.

admin.site.register(LikedSong)
admin.site.register(Playlist)