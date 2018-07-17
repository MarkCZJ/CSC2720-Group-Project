from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'movies'
urlpatterns = [
    # /movies/
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('search', views.search, name='search'),
    path('register', views.register, name='register'),
    path('rate', views.rate, name='rate'),
    path('mylist', views.my_list, name='mylist'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('accounts/profile/', views.index, name='index')
    # path('<uuid:pk>/rate', views.rate_movie, name='rate_movie')

    # # /movies/<movie id>/favorite/
    # re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #
    # #/movies/<movie id>/favorite/
    # re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    #
    # re_path(r'all_movies', views.all_movies, name='all_movies'),

]
# urlpatterns += staticfiles_urlpatterns()