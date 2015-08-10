from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import here,plus,math
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chapter_4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'here/$',here),
    url(r'^(\d{1,2})/plus/(\d{1,2})/$',plus),
	url(r'^(\d{1,2})/math/(\d{1,2})/$',math),
	#url(r'^math/?1st=(\d{1,2})&2nd=(\d{1,2})$',math),
	
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
