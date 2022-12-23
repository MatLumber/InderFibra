from django.db import models
import os
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Valor = models.CharField(max_length=50)
    Stock = models.IntegerField()
    photo = models.ImageField(upload_to = 'Principal/static/imgProductos',unique=False, height_field = None, width_field = None, max_length = 100, help_text = None)
    Ventas = models.IntegerField(default=0)
    Marca = models.CharField(max_length=25)
    Descripcion = models.TextField(max_length=250)
    Modelo = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.Nombre
    def filename(self):
        return os.path.basename(self.photo.name)
class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Cantidad = models.IntegerField()
    Producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)