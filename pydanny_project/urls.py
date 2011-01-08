from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',

    (r'^nimda/', include(admin.site.urls)),
    
    #(r'^$', direct_to_template, {"template":"base.html"}),
    (r'^$', direct_to_template, 
            {"template":"home.html"}),
url(r"", include("staticfiles.urls")),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )