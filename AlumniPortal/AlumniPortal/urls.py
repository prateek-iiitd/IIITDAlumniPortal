from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AlumniPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'AlumniPortal.views.home'),
    url(r'^directory/$', 'AlumniPortal.views.directory'),
    url(r'^contact_us/$', 'AlumniPortal.views.contact_us'),
    url(r'^blog/$', 'AlumniPortal.views.blog'),
    url(r'^news/$', 'AlumniPortal.views.news'),
)
