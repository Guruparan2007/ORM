from django.db import models
from django.contrib import admin
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    rating = models.FloatField()

class MovieAdmin(admin.ModelAdmin):
    list_display = ("movie_id","title","genre","release_year","director","rating")


