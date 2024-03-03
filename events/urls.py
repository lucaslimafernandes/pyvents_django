from django.urls import path
from . import views

urlpatterns = [
    path('', views.vw_events_list, name='vw_events_list'),
]