from django.conf.urls import url
from django.contrib import admin

from nunucast import views as nunucast_views
from . import views

urlpatterns = [
    url(r'^$', nunucast_views.IndexView.as_view(), name='index'),
    url(r'^signup$', nunucast_views.SignUpView.as_view(), name='signup'),
    url(r'^signup/done$', nunucast_views.RegisteredView.as_view(), name='create_user_done'),
]