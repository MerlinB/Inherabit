from django.conf.urls import url
from .views import signup_view

app_name = 'dms'

urlpatterns = [
    url(r'^$', signup_view, name='dms_start'),
]
