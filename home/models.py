from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)
=======

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
>>>>>>> ff136ca41d4557963a8e55a041aba5c7619bc678

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
class Marca (models.Model):
    nombre = models.CharField(max_length= 100)

    def __str__ (self):
        return self.nombre
    
class Producto (models.Model):

=======
class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
>>>>>>> ff136ca41d4557963a8e55a041aba5c7619bc678
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
<<<<<<< HEAD
    categorias = models.ManyToManyField(Categoria, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to ='productos/', null=True, blank=True) #foto opcional

    def __str__ (self):
        return self.nombre
    
class Perfil (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles', null=True, blank=True)
    nombre = models.CharField(max_length= 100)

    def __str__ (self):
        return self.user.username
=======
    Categoria = models.ManyToManyField(Categoria, null=True, blank=True)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
>>>>>>> ff136ca41d4557963a8e55a041aba5c7619bc678
