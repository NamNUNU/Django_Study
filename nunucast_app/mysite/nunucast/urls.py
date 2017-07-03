from django.conf.urls import url
from django.contrib import admin

from nunucast import views as nunucast_views
from . import views

urlpatterns = [
    url(r'^$', nunucast_views.IndexView.as_view(), name='index'),
    
]