from django.urls import path
from Usuarios import views


urlpatterns = {
    path("prueba/<searchString>/<time>/<index>/<oTypeList>/<maxResultsNum>", views.search, name="prueba"),

}