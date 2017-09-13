from django.conf.urls import url
from .views import home_view, start_view, faq_view, about_view

app_name = 'landingpage'

urlpatterns = [
    url(r'^$', start_view, name='start'),
    url(r'^home$', home_view, name='home'),
    url(r'^faq$', faq_view, name='faq'),
    url(r'^about$', about_view, name='about'),
]
