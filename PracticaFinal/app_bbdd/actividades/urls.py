from django.contrib import admin
from django.urls import path,include
from django.urls import path
from .. import views

urlpatterns = [
    path('', views.lista_actividades, name='lista_actividades'),
    path('nueva/', views.crear_actividad, name='crear_actividad'),
    path('<int:id>/', views.detalle_actividad, name='detalle_actividad'),
    path('<int:id>/editar/', views.editar_actividad, name='editar_actividad'),
    path('<int:id>/eliminar/', views.eliminar_actividad, name='eliminar_actividad'),
    path('<int:id>/inscripciones/', views.lista_inscripciones, name='lista_inscripciones'),
    path('<int:id>/inscribir/', views.inscribir_usuario, name='inscribir_usuario'),
    path('<int:id>/inscripciones/<int:usuario_id>/eliminar/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]