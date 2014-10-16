from django.conf.urls import patterns, include, url

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
    url(r'^addNews/$', 'AlumniPortal.views.add_news'),
    url(r'^addEvent/$', 'AlumniPortal.views.add_event'),
    url(r'^addDirectory/$', 'AlumniPortal.views.add_directory'),
)