from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('iati.views',
    url(r'^split/(.*?)$', 'split'),
)
