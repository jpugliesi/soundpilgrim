from django.shortcuts import render
from django.http import HttpResponse

from musicblog.models import SongPost, Genre

def chill(request):
    recent_songposts = get_recent_songposts('Chill', 10)
    return HttpResponse("You're looking at the Chill posts.")

def funky(request):
    recent_songposts = get_recent_songposts('Funky', 10)
    return HttpResponse("You're looking at the Funky posts.")

def indie(request):
    recent_songposts = get_recent_songposts('Indie', 10)
    return HttpResponse("You're looking at the Indie/Alternative posts.")

def rap(request):
    recent_songposts = get_recent_songposts('Rap', 10)
    return HttpResponse("You're looking at the Rap posts.")

def party(request):
    recent_songposts = get_recent_songposts('Party', 10)
    return HttpResponse("You're looking at the Party posts.")

def get_recent_songposts(genre, num_posts_to_grab):
    g = Genre.objects.get(genre_name__contains=genre)
    recent_songposts = g.songpost_set.all().order_by('-created_on')[:num_posts_to_grab]
    return recent_songposts
