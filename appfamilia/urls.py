from django.urls import path
from appfamilia.views import listadoFamiliares

urlpatterns = [
    path("", listadoFamiliares)
]