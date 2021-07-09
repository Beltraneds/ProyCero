from django.contrib import admin
#importar los modelos 
from .models import Categoria, Obra, Galeria, Contacto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Obra)
admin.site.register(Galeria)
admin.site.register(Contacto)