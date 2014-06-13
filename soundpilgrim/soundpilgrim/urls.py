from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soundpilgrim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^genre/', include('musicblog.urls', namespace="musicblog")),
    url(r'^admin/', include(admin.site.urls)),
)
