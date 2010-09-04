from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

import feedparser

def fetch_entries():
    d = feedparser.parse(settings.BLOGGER_TARGET)
    return d["entries"]


urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    
    #(r'^$', direct_to_template, {"template":"base.html"}),
    (r'^$', direct_to_template, 
            {"template":"blogger.html",
                "extra_context": {"entries":fetch_entries()}
            }),

)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )