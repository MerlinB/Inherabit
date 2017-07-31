from django.conf.urls import url
from .views import dashboard_view

app_name = 'dms'

urlpatterns = [
    url(r'^$', dashboard_view, name='dashboard'),
]
