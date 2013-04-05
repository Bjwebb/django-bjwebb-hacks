from django.conf.urls import patterns, include, url

urlpatterns = patterns('whorunsthatbus.views',
    url(r'^$', 'home', name='home'),
)
