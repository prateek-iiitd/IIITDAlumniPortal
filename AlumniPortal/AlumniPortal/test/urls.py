__author__ = 'ankur'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AlumniPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^temp/$', 'AlumniPortal.test.test_views.hello'),
    url(r'^formtest/$', 'AlumniPortal.test.test_views.form_test'),

)

