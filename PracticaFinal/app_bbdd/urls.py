from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('actividades/', include('app_bbdd.actividades.urls')),
    path('usuarios/', include('app_bbdd.usuarios.urls')),
    path('salas/', include('app_bbdd.salas.urls')),
    path('monitores/', include('app_bbdd.monitores.urls')),
]