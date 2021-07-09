from django.db import models
from django.db.models.base import Model

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=25)
    imagen = models.ImageField(upload_to='cate',null=True)
    def __str__(self):
        return self.nombre

class Obra(models.Model):
    nombre = models.CharField(primary_key=True,max_length=30)
    historia = models.TextField()
    descripcion = models.TextField()
    tecnica = models.CharField(max_length=60)
    precio = models.TextField()
    imagen = models.ImageField(upload_to='fotos',default='fotos/no_disponible.jpg')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicar = models.BooleanField(default=False)
    comentario = models.TextField(default='--',null=True)
    artista = models.CharField(max_length=60,default="--", null=True)

    def __str__(self):
        return self.nombre+" - "+str(self.publicar)+" - "+self.comentario 

class Galeria(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='galeria')
    obra = models.ForeignKey(Obra,on_delete=models.CASCADE)

    def __str__(self):
        return "Número: "+str(self.auto_inc)

class Contacto(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=50)
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    mensaje = models.TextField(default='--')

    def __str__(self):
        return "Número: "+str(self.auto_inc)+" - "+self.asunto
        