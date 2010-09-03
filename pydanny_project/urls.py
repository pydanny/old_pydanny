from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()


def fetch_blog():
    target = settings.BLOGGER_TARGET    


urlpatterns = patterns('',
    # Example:
    # (r'^pydanny_project/', include('pydanny_project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', direct_to_template, {"template":"base.html"}),
    #(r'^blogger/$', direct_to_template, {"template":"blogger.html"}),    
    (r'^$', direct_to_template, {"template":"blogger.html"
    }),
    
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )