from django.urls import path 
from .views import vista_about
from .views import vista_biografia
from .views import vista_inicio

urlpatterns = [
    path ('inicio/', vista_inicio),
    path ('about/', vista_about),
    path ('bio/', vista_biografia)
]