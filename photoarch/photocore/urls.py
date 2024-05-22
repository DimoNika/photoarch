from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("storage/", views.storage_view, name="storage"),
]
