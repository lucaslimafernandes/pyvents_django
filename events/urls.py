from django.urls import path
from . import views

urlpatterns = [
    path("", views.vw_events_list, name="vw_events_list"),
    path("event/new", views.vw_new_event, name="vw_new_event"),
]
