from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/whorunsthatbus/', permanent=False)),
    url(r'^iati/', include('iati.urls')),
    url(r'^whorunsthatbus/', include('whorunsthatbus.urls')),
    url(r'^mbtilesmap/', include('mbtilesmap.urls', namespace='mb', app_name='mbtilesmap')),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
