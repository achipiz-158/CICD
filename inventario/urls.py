from django.urls import path
from .views import ListarProveedorView


urlpatterns = [
    path('proveedor/', ListarProveedorView.as_view(), name='proveedor'),
]