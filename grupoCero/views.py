from django.contrib import auth
from django.db.models.fields import EmailField
from django.shortcuts import render
#importe de modelos de tabla
from .models import Categoria, Obra, Galeria
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_aut
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request): #peticion
    obras = Obra.objects.filter(publicar=True).order_by('nombre')[:3]
    categorias = Categoria.objects.all()
    contexto = {"obras":obras,"categorias":categorias}
    return render(request, "index.html",contexto)

def productos(request):
    obras = Obra.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    contexto = {"obras":obras,"categorias":categorias}
    return render(request, "productos.html",contexto)

def filtro_cate(request, id):
    categorias = Categoria.objects.all()
    obj_cate = Categoria.objects.get(nombre=id)
    obras = Obra.objects.filter(categoria=obj_cate).filter(publicar=True)
    cant = Obra.objects.filter(categoria=obj_cate).filter(publicar=True).count()
    contexto = {"obras":obras,"categorias":categorias,"cantidad":cant,"texto":" Producto(s)"}
    return render(request, "productos.html",contexto)

def filtro_categoria(request):
    obras = Obra.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    cant = Obra.objects.filter(publicar=True).count()
    if request.POST:
        categoria = request.POST.get("cboCategoria")
        obj_cate = Categoria.objects.get(nombre=categoria)
        obras = Obra.objects.filter(categoria=obj_cate).filter(publicar=True)
        cant = Obra.objects.filter(categoria=obj_cate).filter(publicar=True).count()
    contexto = {"obras":obras,"categorias":categorias,"cantidad":cant,"texto":" Producto(s)"}
    return render(request, "productos.html",contexto)

def buscar_artista(request):
    obras = Obra.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    if request.POST:
        nombre = request.POST.get("txtNombre")
        obras = Obra.objects.filter(artista=nombre).filter(publicar=True)
    contexto = {"obras":obras,"categorias":categorias}
    return render(request, "productos.html",contexto)

def filtro_concepto(request):
    obras = Obra.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    if request.POST:
        desc = request.POST.get("txtConc")
        obras = Obra.objects.filter(descripcion__contains=desc).filter(publicar=True)
    contexto = {"obras":obras,"categorias":categorias}
    return render(request, "productos.html",contexto)

def informacion(request, id):
    obra = Obra.objects.get(nombre=id)
    galeria = Galeria.objects.filter(obra = obra)
    contexto = {"obra":obra,"galeria":galeria}
    return render(request,"informacion.html",contexto)

def artistas(request):
    return render(request, "artistas.html")

def login(request):
    categorias = Categoria.objects.all()
    contexto = {"categorias":categorias}
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        password = request.POST.get("txtPass")
        us = authenticate(request,username=nombre,password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request,"index.html",contexto)
        else:
            contexto = {"mensaje":"Correo o contraseña incorrecto","categorias":categorias}
            return render(request, "inicio_sesion.html",contexto)
    return render(request, "inicio_sesion.html")

def cerrar_sesion(request):
    categorias = Categoria.objects.all()
    contexto = {"categorias":categorias}
    logout(request)
    return render(request,"index.html",contexto)

def crear_cuenta(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        email = request.POST.get("txtEmail")
        pass1 = request.POST.get("txtPass")
        pass2 = request.POST.get("txtPass2")
        if pass1 != pass2:
            contexto = {"mensaje":"Las contraseñas son diferentes"}
            return render(request, "crear_cuenta.html",contexto)
        
        try:
            usu = User.objects.get(username=nombre)
            contexto = {"mensaje":"El nombre de usuario ya existe"}
            return render(request, "crear_cuenta.html",contexto)
        except:
            usu = User()
            usu.username=nombre
            usu.email=email
            usu.first_name=nombre
            usu.set_password(pass1)
            usu.save()

            us = authenticate(request,username=nombre,password=pass1)
            login_aut(request, us)

            categorias = Categoria.objects.all()
            contexto = {"categorias":categorias}
            return render(request, "index.html",contexto)

    return render(request, "crear_cuenta.html")

def contacto(request):
    return render(request, "contacto.html")

@login_required(login_url='/login/')
@permission_required('grupoCero.add_obra',login_url='/login/')
def publicar(request):
    registros = Categoria.objects.all()
    cantidad= Obra.objects.filter(artista=request.user.username).count()
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        hist = request.POST.get("txtHistoria")
        desc = request.POST.get("txtDesc")
        tecnica = request.POST.get("txtTecnica")
        precio = request.POST.get("txtPrecio")
        cate = request.POST.get("cboCategoria")
        ima = request.FILES.get("txtImg")
        obj_cate = Categoria.objects.get(nombre=cate)
        try:
            obr = Obra.objects.get(nombre=nombre)
            mensaje="La obra ya existe"
        except:
            obr = Obra()
            obr.nombre=nombre
            obr.historia=hist
            obr.descripcion=desc
            obr.tecnica=tecnica
            obr.precio=precio
            if ima is not None:
                obr.imagen = ima
            obr.categoria=obj_cate
            obr.artista = request.user.username #Recupero del request el usuario (login)
            mensaje="Obra Guardada"
            obr.save()

    obras = Obra.objects.filter(artista=request.user.username)
    cantidad= Obra.objects.filter(artista=request.user.username).count()
    contexto = {"categorias":registros,"mensaje":mensaje,"obras":obras,"cantidad":cantidad}

    return render(request, "publicar.html",contexto)

@login_required(login_url='/login/')
@permission_required('grupoCero.delete_obra',login_url='/login/')
def eliminar_obra(request, id):
    mensaje=""
    try:
        obr = Obra.objects.get(nombre=id)
        obr.delete()
        mensaje = "Obra eliminada"
    except:
        mensaje="Obra no eliminada"

    registros = Categoria.objects.all()
    obras = Obra.objects.filter(artista=request.user.username)
    contexto = {"categorias":registros,"mensaje":mensaje,"obras":obras}
    cantidad = Obra.objects.filter(artista = request.user.username).count()
    contexto["cantidad"] = cantidad
    return render(request, "publicar.html",contexto)

@login_required(login_url='/login/')
@permission_required('grupoCero.change_obra',login_url='/login/')
def modificar_obra(request, id):
    obr = Obra.objects.get(nombre=id)   
    registros = Categoria.objects.all()  
    contexto = {"categorias":registros,"obra":obr}
    return render(request, "modificar.html",contexto)

@login_required(login_url='/login/')
@permission_required('grupoCero.change_obra',login_url='/login/')
def modificacion(request):
    mensaje=""
    nom_user = request.user.username
    if request.POST:
        nombre = request.POST.get("txtNombre")
        hist = request.POST.get("txtHistoria")
        desc = request.POST.get("txtDesc")
        tecnica = request.POST.get("txtTecnica")
        precio = request.POST.get("txtPrecio")
        cate = request.POST.get("cboCategoria")
        ima = request.FILES.get("txtImg")
        obj_cate = Categoria.objects.get(nombre=cate)

        try:
            obr = Obra.objects.get(nombre=nombre)
            obr.historia = hist
            obr.descripcion = desc
            obr.tecnica = tecnica
            obr.precio = precio
            if ima is not None:
                obr.imagen = ima
            obr.categoria = obj_cate
            obr.comentario ='--'

            obr.save()
            mensaje = "Ha modificado la obra: "+nombre
        except:
            mensaje="No se modificó la obra: "+nombre

    registros = Categoria.objects.all()
    obras = Obra.objects.filter(artista=nom_user)
    contexto = {"categorias":registros,"mensaje":mensaje,"obras":obras}
    return render(request, "publicar.html",contexto)

def insertar_galeria(request):
    mensaje = ""
    if request.POST:
        nom_obra = request.POST.get("txtObra")
        imagen = request.FILES.get("txtImg")
        obj_obra = Obra.objects.get(nombre = nom_obra)

        gale = Galeria()
        gale.imagen = imagen
        gale.obra = obj_obra
        gale.save()
        mensaje = "Agregó una imágen para la obra "+nom_obra
     
    obras = Obra.objects.filter(artista=request.user.username)
    registros = Categoria.objects.all()
    contexto = {"categorias":registros,"mensaje":mensaje,"obras":obras}
    cantidad = Obra.objects.filter(artista = request.user.username).count()
    contexto["cantidad"] = cantidad
    return render(request, "publicar.html",contexto)