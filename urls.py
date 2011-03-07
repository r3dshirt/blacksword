from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/sam/Projects/blacksword/blacksword/site_media/'}),
    (r'^kin-events/', 'kin_events.views.index'),
    (r'^about.html', 'home.views.about' ),
    (r'^', 'home.views.index'),
)