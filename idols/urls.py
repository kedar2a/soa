from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_slider, name='home_slider'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^aim$', views.aim, name='aim'),
    url(r'^media$', views.media, name='media'),
    url(r'^team$', views.team, name='team'),
    url(r'^contact$', views.contact, name='contact'),
]