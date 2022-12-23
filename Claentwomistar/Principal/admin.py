from django.contrib import admin
from Administracion.models import Productos
# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nombre']
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('Valor','Stock','Ventas')}
            ),
        )
admin.site.register(Productos, ProductosAdmin)