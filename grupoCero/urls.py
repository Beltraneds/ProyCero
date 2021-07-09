from django.contrib import admin
from django.urls import path, include

from .views import insertar_galeria, modificacion, modificar_obra, eliminar_obra, cerrar_sesion, filtro_cate, filtro_concepto, buscar_artista, filtro_categoria, index, informacion, productos, artistas, login, crear_cuenta, contacto, publicar

urlpatterns = [
    path('',index,name='IND'),
    path('productos/',productos,name='PROD'),
    path('login/',login,name='LOG'),
    path('crear_cuenta/',crear_cuenta,name='CREAC'),
    path('artistas/',artistas,name='ARTI'),
    path('contacto/',contacto,name='CONTA'),
    path('publicar/',publicar,name='PUBLI'),
    path('informacion/<id>/',informacion,name='INFO'),
    path('filtro_categoria/',filtro_categoria,name='FILTROC'),
    path('buscar_artista/',buscar_artista,name='BUSCARA'),
    path('filtro_concepto/',filtro_concepto,name='FILCON'),
    path('filtro_cate/<id>/',filtro_cate,name='FILTROCATE'),
    path('cerrar_sesion/',cerrar_sesion,name='CERRAR'),
    path('eliminar_obra/<id>/',eliminar_obra,name='ELIM'),
    path('modificar_obra/<id>/',modificar_obra,name='MODI'),
    path('modificacion/',modificacion,name='MODIFI'),
    path('insertar_galeria/',insertar_galeria,name='INSERTARG'),
]
