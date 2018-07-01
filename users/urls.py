from django.conf.urls import url
from users.views import *

urlpatterns=[
    url(r'signup/', signup, name='signup'),
    url(r'login/', auth_login, name='login'),
    url(r'logout', auth_logout, name='logout')
]