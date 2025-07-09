from django.contrib import admin
from django.urls import path
from evaluador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nuevo/', views.agregar_candidato, name='nuevo_candidato'),
    path('editar/<int:id>/', views.editar_candidato, name='editar_candidato'),
    path('eliminar/<int:id>/', views.eliminar_candidato, name='eliminar_candidato'),
]

