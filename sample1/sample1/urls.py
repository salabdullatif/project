from django.conf.urls import patterns, include, url
from django.contrib import admin
from sample1.views import createjob, submitjob

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'createJob/$',createjob),
    url(r'submitJob/$',submitjob),
    url(r'^admin/', include(admin.site.urls)),
)
