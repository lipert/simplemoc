from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'simplemop.core.views.home', name='home'),
     url(r'^contato/$', 'simplemop.core.views.contact', name='contact'),
     url(r'^contatos/$', 'simplemop.core.views.contact', name='contact'),
     url(r'^home/$', 'simplemop.core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
