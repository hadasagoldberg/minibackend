from django.urls import path
from Usuarios import views


urlpatterns = {
    path("prueba/", views.prueba, name="prueba"),



}