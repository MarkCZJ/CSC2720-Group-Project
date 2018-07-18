from django.urls import path
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
    path('edit', views.edit, name='edit'),
    path('mylist', views.my_list, name='mylist'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),

]