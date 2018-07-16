from django.contrib import admin
from .models import Movie, UserRatings
# Register your models here.

admin.site.register(Movie)
admin.site.register(UserRatings)
