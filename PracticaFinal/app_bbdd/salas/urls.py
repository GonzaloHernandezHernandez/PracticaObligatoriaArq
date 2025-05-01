from django.urls import path
from .. import views

urlpatterns = [
    path('', views.lista_salas, name='lista_salas'),
    path('nueva/', views.crear_sala, name='crear_sala'),
    path('<int:id>/', views.detalle_sala, name='detalle_sala'),
    path('<int:id>/editar/', views.editar_sala, name='editar_sala'),
    path('<int:id>/eliminar/', views.eliminar_sala, name='eliminar_sala'),
]