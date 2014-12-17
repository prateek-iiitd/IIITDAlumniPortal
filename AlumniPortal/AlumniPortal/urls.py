from django.conf.urls import patterns, include, url
from AlumniPortal import settings_dev
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AlumniPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', include('AlumniPortal.test.urls')),
    url(r'^$', 'AlumniPortal.views.home'),
    url(r'^directory/$', 'AlumniPortal.views.directory'),
    url(r'^contact_us/$', 'AlumniPortal.views.contact_us'),
    url(r'^blog/$', 'AlumniPortal.views.blog'),
    url(r'^news/$', 'AlumniPortal.views.news'),
    url(r'^directory/batch/$', 'AlumniPortal.views.get_by_batch'),
    url(r'^giveback/$', 'AlumniPortal.views.giveback'),
    url(r'^feedback/$', 'AlumniPortal.views.feedback'),
    url(r'^admin_forms/$', 'AlumniPortal.views.admin_forms'),
    url(r'^admin_forms/add_news/$', 'AlumniPortal.views.add_news'),
    url(r'^admin_forms/add_event/$', 'AlumniPortal.views.add_event'),
    url(r'^admin_forms/add_directory/$', 'AlumniPortal.views.add_directory'),
    url(r'^admin_forms/add_blog/$', 'AlumniPortal.views.add_blog'),
    url(r'^accounts/', include('allauth.urls')),
)

if settings_dev.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings_dev.MEDIA_ROOT}))