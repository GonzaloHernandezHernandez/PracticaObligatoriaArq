from django.urls import path
from .. import views
urlpatterns = [
    path('', views.lista_monitores, name='lista_monitores'),
    path('nuevo/', views.crear_monitor, name='crear_monitor'),
    path('<int:id>/', views.detalle_monitor, name='detalle_monitor'),
    path('<int:id>/editar/', views.editar_monitor, name='editar_monitor'),
    path('<int:id>/eliminar/', views.eliminar_monitor, name='eliminar_monitor'),
]