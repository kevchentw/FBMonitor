from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'FBMonitor.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
                       url(r'^monitor/', 'FBMonitor.views.monitor', name='monitor'),
                       url(r'^monitor_all/', 'FBMonitor.views.monitor_all', name='monitor_all'),
                       url(r'^update/', 'FBMonitor.views.update', name='update'),
                       url(r'^post/', 'FBMonitor.views.post_view', name='post'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
