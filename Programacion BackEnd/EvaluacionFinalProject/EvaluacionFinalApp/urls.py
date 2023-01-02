from django.urls import include,path
from rest_framework import routers
from .views import *

# Definimos un enrutador
router = routers.DefaultRouter()
# Registro de reserva en router
router.register(r'categoria', CategoriaViewSet)
router.register(r'rol', RolViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'distribuidor', DistribuidorViewSet)
router.register(r'producto', ProductoViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'vendedor', VendedorViewSet)
router.register(r'devolucion', DevolucionViewSet)

# URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls'))
]