from django.urls import path
from . import views

urlpatterns = [
    path("account/new", views.vw_acc_new, name="vw_acc_new"),
]
