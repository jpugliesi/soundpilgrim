from django.utils import timezone
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse

from musicblog.models import SongPost, Genre

def chill(request, template='musicblog/base_genre.html', page_template='musicblog/base_genre_page.html'):
    recent_songposts = get_recent_songposts('Chill') 
    context = {}
    context.update({'genre': "Chill", 'short_genre': 'chill', 'recent_songposts': recent_songposts, 'page_template': page_template, })
    if request.is_ajax():
        template = page_template

    return render_to_response(template, context, context_instance=RequestContext(request))


def funky(request, template='musicblog/base_genre.html', page_template='musicblog/base_genre_page.html'):
    recent_songposts = get_recent_songposts('Funky') 
    context = {}
    context.update({'genre': "Funky", 'short_genre': 'funky', 'recent_songposts': recent_songposts, 'page_template': page_template, })
    if request.is_ajax():
        template = page_template

    return render_to_response(template, context, context_instance=RequestContext(request))

def indie(request, template='musicblog/base_genre.html', page_template='musicblog/base_genre_page.html'):
    recent_songposts = get_recent_songposts('Indie') 
    context = {}
    context.update({'genre': "Indie & Alternative", 'short_genre': 'indie', 'recent_songposts': recent_songposts, 'page_template': page_template, })
    if request.is_ajax():
        template = page_template

    return render_to_response(template, context, context_instance=RequestContext(request))


def rap(request, template='musicblog/base_genre.html', page_template='musicblog/base_genre_page.html'):
    recent_songposts = get_recent_songposts('Rap') 
    context = {}
    context.update({'genre': "Rap", 'short_genre': 'rap', 'recent_songposts': recent_songposts, 'page_template': page_template, })
    if request.is_ajax():
        template = page_template

    return render_to_response(template, context, context_instance=RequestContext(request))


def party(request, template='musicblog/base_genre.html', page_template='musicblog/base_genre_page.html'):
    recent_songposts = get_recent_songposts('Party') 
    context = {}
    context.update({'genre': "Party", 'short_genre': 'party', 'recent_songposts': recent_songposts, 'page_template': page_template, })
    if request.is_ajax():
        template = page_template

    return render_to_response(template, context, context_instance=RequestContext(request))
    

def all_music(request, template='musicblog/base_genre.html', page_template='musicblog/base_genre_page.html'):
    recent_songposts = get_recent_songposts('All') 
    context = {}
    context.update({'genre': "All Music", 'short_genre': 'all_music', 'recent_songposts': recent_songposts, 'page_template': page_template, })
    if request.is_ajax():
        template = page_template

    return render_to_response(template, context, context_instance=RequestContext(request))

def get_recent_songposts(genre):
    if genre != 'All':
        g = Genre.objects.get(genre_name__contains=genre)
        recent_songposts = g.songpost_set.filter(created_on__lte=timezone.now()).order_by('-created_on')
    else:
        recent_songposts = SongPost.objects.all().order_by('-created_on')
    return recent_songposts
