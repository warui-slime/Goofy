from django.urls import path
from . import views as goofyviews


urlpatterns = [
    path("",goofyviews.home,name="home"),
    path("getHomedata/",goofyviews.getHomedata,name="getHomedata"),
    path("explore/",goofyviews.explore,name="explore"),
    path("mylikes/",goofyviews.likes,name="mylikes"),
    path("library/",goofyviews.library,name="library"),
    path("profile/",goofyviews.profile,name="profile"),
    path("getExploredata/",goofyviews.getExploredata,name="getExploredata"),
    path("getSuggestions/",goofyviews.getSuggestions,name="getSuggestions"),
    path("getSong/",goofyviews.getSong,name="getSong"),
    path("getSearch/",goofyviews.getSearch,name="getSearch"),
    path("getPlaylist/",goofyviews.getPlaylist,name="getPlaylist"),
    path("getAlbum/",goofyviews.getAlbum,name="getAlbum"),
    path("getArtist/",goofyviews.getArtist,name="getArtist"),
    path("getMoodpl/",goofyviews.getMoodpl,name="getMoodpl"),
    path("getRelated/",goofyviews.getRelated,name="getRelated"),
    path('like/', goofyviews.like_song, name='like_song'),
    path('unlike/', goofyviews.unlike_song, name='unlike_song'),
    path('getlikedsongs/', goofyviews.getLikedSongs, name='getlikedsongs'),
    path('getLikedata/', goofyviews.getLikedata, name='getLikedata'),
    path('getmusicblob/', goofyviews.createFileResponse, name='getmusicblob'),
    path('getPlaylists/', goofyviews.getPlaylists, name='getPlaylists'),
    path('createPlaylist/', goofyviews.createPlaylist, name='createPlaylist'),
    path('updatePlaylist/', goofyviews.updatePlaylist, name='updatePlaylist'),
    path('deletePlaylist/', goofyviews.deletePlaylist, name='deletePlaylist'),
    path('getPlaylistData/', goofyviews.getPlaylistData, name='getPlaylistData'),
    path('clearsongs/', goofyviews.clearSongs, name='clearsongs'),
    path('getLyrics/', goofyviews.getLyrics, name='getLyrics'),
    path('getProfileImage/',goofyviews.getProfileImage,name='getProfileImage'),
    path('updateProfileImage/',goofyviews.updateProfileImage,name='updateProfileImage')
]