# usr/bin/python3
"""
My blog urls
"""
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this is not sure - for adding pictures
