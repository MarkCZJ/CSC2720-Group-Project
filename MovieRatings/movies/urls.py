from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'movies'
urlpatterns = [
    # /movies/
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('register', views.register, name='register'),

    # # /movies/<movie id>/favorite/
    # re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #
    # #/movies/<movie id>/favorite/
    # re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    #
    # re_path(r'all_movies', views.all_movies, name='all_movies'),

]
urlpatterns += staticfiles_urlpatterns()