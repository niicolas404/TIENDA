from django.contrib import admin
from .models import Cliente, pedido


# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'direccion']
    list_filter = ['nombre', 'email']
    search_fields = ['nombre', 'email']

class pedidoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'url', 'cliente', 'fecha', 'cantidad', 'total_formatted']
    list_filter = ['producto', 'cliente', 'fecha', 'cantidad']
    search_fields = ['producto', 'cliente__nombre']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(pedido, pedidoAdmin)
