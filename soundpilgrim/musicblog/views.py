from django.shortcuts import render
from django.http import HttpResponse

from musicblog.models import SongPost, Genre

def chill(request):
    recent_songposts = get_recent_songposts('Chill', 10)
    context = {'genre': "Chill", 'short_genre': 'chill', 'recent_songposts': recent_songposts}
    return render(request, 'musicblog/base_genre.html', context)

def funky(request):
    recent_songposts = get_recent_songposts('Funky', 10)
    context = {'genre': "Funky", 'short_genre': 'funky', 'recent_songposts': recent_songposts}
    return render(request, 'musicblog/base_genre.html', context)

def indie(request):
    recent_songposts = get_recent_songposts('Indie', 10)
    context = {'genre': "Indie/Alternative", 'short_genre': 'indie', 'recent_songposts': recent_songposts}
    return render(request, 'musicblog/base_genre.html', context)

def rap(request):
    recent_songposts = get_recent_songposts('Rap', 10)
    context = {'genre': "Rap", 'short_genre': 'rap', 'recent_songposts': recent_songposts}
    return render(request, 'musicblog/base_genre.html', context)


def party(request):
    recent_songposts = get_recent_songposts('Party', 10)
    context = {'genre': "Party", 'short_genre': 'party', 'recent_songposts': recent_songposts}
    return render(request, 'musicblog/base_genre.html', context)

def get_recent_songposts(genre, num_posts_to_grab):
    g = Genre.objects.get(genre_name__contains=genre)
    recent_songposts = g.songpost_set.all().order_by('-created_on')[:num_posts_to_grab]
    return recent_songposts
