from django.urls import path
from . import views as homeviews


urlpatterns = [
    path("",homeviews.home,name="home"),
    path("getHomedata/",homeviews.getHomedata,name="getHomedata"),
    path("explore/",homeviews.explore,name="explore"),
    path("mylikes/",homeviews.likes,name="mylikes"),
    path("getExploredata/",homeviews.getExploredata,name="getExploredata"),
    path("getSuggestions/",homeviews.getSuggestions,name="getSuggestions"),
    path("getSong/",homeviews.getSong,name="getSong"),
    path("getSearch/",homeviews.getSearch,name="getSearch"),
    path("getPlaylist/",homeviews.getPlaylist,name="getPlaylist"),
    path("getAlbum/",homeviews.getAlbum,name="getAlbum"),
    path("getArtist/",homeviews.getArtist,name="getArtist"),
    path("getMoodpl/",homeviews.getMoodpl,name="getMoodpl"),
]