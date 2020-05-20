from django.urls import path
from .views import Lista, comprar, cancelarCompra, Carrito, confirmarCompra

app_name = 'articulos'

urlpatterns = [
    path('lista/', Lista.as_view(), name='lista'),
    path('comprar/<int:pk>', comprar, name='comprar'),

    path('cancelarCompra/', cancelarCompra, name='cancelarCompra'),
    path('confirmarCompra/', confirmarCompra, name='confirmarCompra'),
    
    path('carrito/', Carrito.as_view(), name='carrito'),

]
