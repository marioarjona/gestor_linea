"""
URL configuration for gestor_linea project.

Las rutas de la app 'produccion' se incluyen desde produccion/urls.py.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("produccion.urls")),
]
