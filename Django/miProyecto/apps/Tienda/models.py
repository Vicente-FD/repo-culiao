from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(primary_key=True, max_length=50)
    contrasena = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.usuario
    
class Producto(models.Model):
    sku = models.CharField(primary_key=True, max_length=50)
    nombreProd = models.CharField(max_length=50, null=False)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    precio = models.IntegerField(null=False)
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        txt = "N° {0} - Nombre: {1} - Stock: {2} - Precio: {3} - Fecha: {4}"
        return txt.format(self.sku,self.nombreProd,self.fecha_vencimiento, self.precio, self.image_url)
    
class Categoria(models.Model):
    categoria = models.CharField(primary_key=True, max_length=50)
    descripcion = models.CharField(max_length=50, null=False)
    productos = models.ManyToManyField(Producto)
    
    def __str__(self):
        return self.categoria
        
