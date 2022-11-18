from django.urls import path
from Usuarios import views


urlpatterns = {
    path("search/<link>", views.search, name="search"),
    path("ftsearch/<link>", views.ftsearch, name="ftsearch"),
    path("regen/<link>", views.regen, name="regen"),
    path("regenarea/<link>", views.regenarea, name="regenarea"),
    path("update/<link>", views.update, name="update"),
    path("traverse/<link>", views.traverse, name="traverse"),
    path("oread/<link>", views.oread, name="oread"),
    path("val/<link>", views.val, name="val"),
    path("updateconfig/<link>", views.updateconfig, name="updateconfig"),
    path("getconfig/<link>", views.getconfig, name="getconfig"),
    path("getconfigfo/<link>", views.getconfigfo, name="getconfigfo")

}
