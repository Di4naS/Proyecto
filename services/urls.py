from django.urls import path, include
from rest_framework import routers
from home.models import *
from services.views import *

router = routers.DefaultRouter()
router.register(r'productos', producto_viewset)
router.register(r'marcas', marca_viewset)
router.register(r'categorias', categoria_viewset)

urlpatterns = [
        path('', include(router.urls)),
]