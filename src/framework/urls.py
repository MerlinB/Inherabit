from django.conf.urls import url
from .views import signup_view, login_view, logout_view

app_name = 'framework'

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^signup/$', signup_view, name='signup'),
]
