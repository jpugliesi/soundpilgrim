from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soundpilgrim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'soundpilgrim.views.home', name='home'),
    url(r'^genre/', include('musicblog.urls', namespace="musicblog")),
    url(r'^quotes/', include('quotes.urls', namespace="quotes")),
    url(r'^admin/', include(admin.site.urls)),
)
