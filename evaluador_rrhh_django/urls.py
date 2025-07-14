from django.contrib import admin
from django.urls import path,include
from evaluador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nuevo/', views.agregar_candidato, name='nuevo_candidato'),
    path('editar/<int:id>/', views.editar_candidato, name='editar_candidato'),
    path('eliminar/<int:id>/', views.eliminar_candidato, name='eliminar_candidato'),
    path('puestos/', views.listar_puestos, name='listar_puestos'),
    path('puestos/nuevo/', views.crear_puesto, name='crear_puesto'),
    path('puestos/postular/<int:puesto_id>/', views.postular_puesto, name='postular_puesto'),
    path('postulaciones/', views.ver_postulaciones, name='ver_postulaciones'),
    path("perfiles/", views.ver_perfiles, name="ver_perfiles"),
    path('resumen/', views.resumen_candidatos, name='resumen_candidatos'),
]

