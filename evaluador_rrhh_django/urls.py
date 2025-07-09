from django.contrib import admin
from django.urls import path
from evaluador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nuevo/', views.agregar_candidato, name='nuevo_candidato'),
]

