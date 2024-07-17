from django.urls import path
from . import views as homeviews
from users import views as userviews

urlpatterns = [
    path("",homeviews.home,name="home"),
    path("getHomedata/",homeviews.getHomedata,name="getHomedata"),
    path("explore/",homeviews.explore,name="explore"),
    path("getExploredata/",homeviews.getExploredata,name="getExploredata")
]