from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_slider, name='home_slider'),
    
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^gallery/(?P<murti_category_code>[\w-]+)$', views.murti_category, name='murti_category'),
    url(r'^gallery/(?P<murti_category_code>[\w-]+)/(?P<m_id>[\w-]+)$', views.murti_detail, name='murti_detail'),
    url(r'^aim$', views.aim, name='aim'),
    url(r'^media$', views.media, name='media'),
    url(r'^team$', views.team, name='team'),
    url(r'^contact$', views.contact, name='contact'),
]