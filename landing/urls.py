from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
  url(r'^$', views.landing, name='landing'),
  url(r'^time/plus/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),
]


urlpatterns += staticfiles_urlpatterns()