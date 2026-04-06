from django.urls import path
from . import views

urlpatterns = [
    # Vinculamos la función 'inicio' a la raíz de la app
    path('', views.inicio, name='inicio'),
]