from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('eliminar_cliente/<int:idCliente>/', views.eliminar_cliente, name='eliminar_cliente'),
]