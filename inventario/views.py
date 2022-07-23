from django.views.generic import ListView
from django.shortcuts import render
from .models import Proveedor


class ListarProveedorView(ListView):
    template_name = 'listaproveedor.html'
    queryset = Proveedor.objects.all().order_by('-id')