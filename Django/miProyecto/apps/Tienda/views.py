from django.shortcuts import render,redirect
from .models import *
import os
from django.conf import settings

# Create your views here.

def cargarIndex(request):
    return render(request, "index.html")

def cargarCarrito(request):
    return render(request, "carrito2.html")

def cargarSuscripcion(request):
    return render(request, "suscripcion.html")

def cargarNosotras(request):
    return render(request, "nosotras.html")

def cargarTerms(request):
    return render(request, "terms.html")

def agregarProducto(request):
    return render(request, "agregarProducto.html")


def cargarInicio(request):
    productos = Producto.objects.all()
    cate_perros = Producto.objects.filter(categoria_id = 1)
    cate_gatos = Producto.objects.filter(categoria_id = 2)
    return render(request, "inicio.html",{"prod":productos, "cate_perro":cate_perros,"cate_gato":cate_gatos})



def cargarAgregarProducto(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request,"agregarProducto.html",{"cate":categorias, "prod":productos})


def agregarProducto(request):
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_image = request.FILES['txtImg']

    Producto.objects.create(sku = v_sku, nombre= v_nombre, stock = v_stock,precio = v_precio,fecha_vencimiento = v_fecha_vencimiento, image_url = v_image)
    return redirect('/agregarProducto')

def cargarCarrito(request):
    productos = Producto.objects.filter(stock__gt=0)
    cate_perros = Producto.objects.filter(categoria_id=1, stock__gt=0)
    cate_gatos = Producto.objects.filter(categoria_id=2, stock__gt=0)
    return render(request, "carrito.html", {"prod": productos, "cate_perro": cate_perros, "cate_gato": cate_gatos})

def cargarShop(request):
    productos = Producto.objects.filter(stock__gt=0)
    cate_perros = Producto.objects.filter(categoria_id=1, stock__gt=0)
    cate_gatos = Producto.objects.filter(categoria_id=2, stock__gt=0)
    return render(request, "shop.html", {"prod": productos, "cate_perro": cate_perros, "cate_gato": cate_gatos})