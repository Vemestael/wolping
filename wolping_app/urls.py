from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update', views.update, name='update'),
    path('ping', views.ping, name='ping'),
    path('wol', views.wake_on_lan, name='wol'),
]
