from django.shortcuts import render

from .models import pedido


def inicio(request):
    pedidos = pedido.objects.select_related('cliente').order_by('-fecha', '-id')
    return render(request, 'inicio.html', {'pedidos': pedidos})
