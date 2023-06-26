from django.urls import path
from . import views

urlpatterns = [
    path('',views.cargarIndex),
    path('carrito2',views.cargarCarrito),
    path('suscripcion',views.cargarSuscripcion),
    path('nosotras',views.cargarNosotras),
    path('terms',views.cargarTerms),
    path('agregarProducto',views.agregarProducto),
    path('agregarProducto/<str:sku>',views.agregarProducto),
]

