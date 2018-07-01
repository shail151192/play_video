from django.conf.urls import url
from home.views import *

urlpatterns = [
    url(r'videos', home_page, name='view home'),
    url(r'upload', upload, name='upload video'),
    url(r'play/(?P<id>\d+)/$', play, name='play_video')
]