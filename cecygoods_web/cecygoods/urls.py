from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('ubicaciones/', views.UbicacionesListView.as_view(), name='ubicaciones'),
    path('servicios/', views.ServiciosListView.as_view(), name='servicios'),

  
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registrar, name='registro'),
    path('salir/', views.cerrar_sesion, name='salir'),
    path('panel/', views.panel_estudiante, name='panel_estudiante'),
    path('reportar/', views.reportar_problema, name='reportar_problema'),
    path('sugerencias/', views.sugerencias, name='sugerencias'),
    path('perfil/', views.perfil, name='perfil'),

   
    path('admin-panel/', views.admin_metricas, name='admin_metricas'),
    path('admin-usuarios/', views.AdminUsuariosListView.as_view(), name='admin_usuarios'),
    path('borrar-usuario/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    
    path('admin-catalogo/', views.AdminCatalogoListView.as_view(), name='admin_catalogo'),
    path('servicio/nuevo/', views.CrearServicioView.as_view(), name='crear_servicio'),
    path('servicio/editar/<int:pk>/', views.EditarServicioView.as_view(), name='editar_servicio'),
    path('servicio/borrar/<int:pk>/', views.EliminarServicioView.as_view(), name='eliminar_servicio'),

    path('admin-incidencias/', views.AdminIncidenciasListView.as_view(), name='admin_incidencias'),
    path('incidencia/borrar/<int:pk>/', views.EliminarIncidenciaView.as_view(), name='eliminar_incidencia'),
    path('admin-buzon/', views.AdminBuzonListView.as_view(), name='admin_buzon'),
]
