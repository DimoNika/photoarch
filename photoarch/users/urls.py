from django.urls import path
from . import views
app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("registre/", views.registre_view, name="registre")
]
