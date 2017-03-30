from django.conf.urls import url
from .views import home_view, start_view

app_name = 'landingpage'

urlpatterns = [
    url(r'^$', start_view, name='start'),
    url(r'^home$', home_view, name='home'),
]
