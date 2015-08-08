from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import here
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chapter_4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'here/$',here),
)
