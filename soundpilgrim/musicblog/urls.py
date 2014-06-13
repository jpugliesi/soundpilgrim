from django.conf.urls import patterns, url

from musicblog import views

urlpatterns = patterns('',
    url(r'^chill/', views.chill, name='chill'),
    url(r'^funky/', views.funky, name='funky'),
    url(r'^indie/', views.indie, name='indie'),
    url(r'^rap/', views.rap, name='rap'),
    url(r'^party/', views.party, name='party'),
)
