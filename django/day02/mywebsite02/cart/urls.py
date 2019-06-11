from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^var/$', views.var_views),
    url(r'^filter/$', views.filter_views),
    url(r'^static/$', views.static_views),
    url(r'^base/$', views.base_views),
    url(r'^child/$', views.child_views, name='123'),
]
