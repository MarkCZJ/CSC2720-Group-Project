from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Movie, UserRatings
from django.contrib.auth.forms import UserCreationForm


def index(request):
    all_movies = Movie.objects.all()

    context = {
        'all_movies': all_movies,
    }

    return render(request, 'movies/index.html', context)

    return render(request, 'movies/search.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('movies:index')
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})


def search(request):
    if request.method == 'GET':
        movie = request.GET.get('query')
        if len(movie) == 0:
            found_movies = Movie.objects.order_by('movie_title')
            return render(request, 'movies/search.html', {'found_movies': found_movies})
        try:
            found_movies = Movie.objects.filter(movie_title__contains=movie)
            found_movies = found_movies.order_by('title_year')
            return render(request, 'movies/search.html', {'found_movies': found_movies})
        except:
            return render(request, 'movies/search.html', {})


def rate(request):
    if request.user.id is None:
        return render(request, 'movies/index.html', {})


    if request.method == 'POST':
        user_id = request.user.id
        movie = request.POST.get('movie')
        year = request.POST.get('year')
        user_rating = request.POST.get('rating')
        if user_rating == '':
            return redirect('movies:index')
        existing_rating = UserRatings.objects.filter(user=user_id,
                                                     movie_title=movie,
                                                     title_year=year)
        if len(existing_rating) == 0:
            obj, creates = UserRatings.objects.get_or_create(
                user=user_id,
                movie_title=movie,
                title_year=year,
                rating=user_rating
            )
        else:
            edit(request)
    return redirect('movies:mylist')


def edit(request):
    if request.user.id is None:
        return render(request, 'movies/index.html', {})
    if request.method == 'GET':
        form = request.GET.__str__()
    if request.method == 'POST':
        user_id = request.user.id
        movie = request.POST.get('movie')
        year = request.POST.get('year')
        user_rating = request.POST.get('rating')
        if user_rating == '':
            return redirect('movies:index')
        existing_rating = UserRatings.objects.get(user=user_id,
                                                  movie_title=movie,
                                                  title_year=year)
        existing_rating.rating = user_rating
        existing_rating.save()
    return redirect('movies:mylist')


def my_list(request):
    if request.method == 'GET':
        user_id = request.user.id

        try:
            ratings = UserRatings.objects.filter(user__exact=user_id)
            context = {
                'found_ratings': ratings,
            }
            return render(request, 'movies/mylist.html', {'found_movies': ratings})
        except:
            return render(request, 'movies/search.html', {})
