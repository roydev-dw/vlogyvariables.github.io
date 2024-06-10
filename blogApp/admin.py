from django.contrib import admin
from .models import Articulo, Categoria

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'fecha_actualizacion', 'publicado')
    list_filter = ('autor', 'fecha_creacion', 'fecha_actualizacion')

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria)

