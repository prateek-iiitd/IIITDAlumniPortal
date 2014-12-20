__author__ = 'ankur'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AlumniPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^temp/$', 'AlumniPortal.test.test_views.hello'),
    url(r'^formtest/$', 'AlumniPortal.test.test_views.form_test'),
    url(r'^adminformtest', 'AlumniPortal.test.test_views.admin_form_test'),
    url(r'^profile/$', 'AlumniPortal.test.test_views.profile_test'),
    url(r'^profile/edit/personal/$', 'AlumniPortal.test.test_views.profile_edit_personal_test'),
    url(r'^profile/edit/work/$', 'AlumniPortal.test.test_views.profile_edit_work_test'),
    url(r'^profile/edit/education/$', 'AlumniPortal.test.test_views.profile_edit_education_test'),
    url(r'^profile/link/$', 'AlumniPortal.test.test_views.profile_link_test'),
    url(r'^give_back/$', 'AlumniPortal.test.test_views.give_back'),
    url(r'^prototype_filter/$', 'AlumniPortal.test.test_views.prototype_filter'),
    url(r'^prototype_result/$', 'AlumniPortal.test.test_views.prototype_result'),
)

