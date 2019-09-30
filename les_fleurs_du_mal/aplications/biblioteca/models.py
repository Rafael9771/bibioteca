from django.db import models

# Create your models here.

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_autor = models.CharField('Nombres', max_length=80)
    apellidos_autor = models.CharField('Apellidos', max_length=80)
    nacionalidad_autor = models.CharField('Nacionalidad', blank=True, max_length=180)
    fecha_creacion_autor = models.DateField()
    fecha_modificacion_autor = models.DateField()
    status_autor = models.CharField('status',blank=False, max_length=1)


    def __str__(self):
        return self.nombre_autor+" "+self.apellidos_autor


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField('Nombre', blank=False, max_length=180)
    descripcion_categoria = models.CharField('Descripcion', blank=False, max_length=300)
    fecha_creacion_categoria = models.DateField()
    fecha_modificacion_categoria = models.DateField()
    status_categoria = models.CharField('status', blank=False, max_length=1)

    def __str__(self):
        return self.nombre_categoria


class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre_editorial = models.CharField('Nombre', blank=False, max_length=180)
    pais_editorial = models.CharField('Pais', blank=False, max_length=300)
    fecha_creacion_editorial = models.DateField()
    fecha_modificacion_editorial = models.DateField()
    status_editorial = models.CharField('status', blank=False, max_length=1)

    def __str__(self):
        return self.nombre_editorial








class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField('Nombre', blank=False, max_length=80)
    descripcion_servicio = models.CharField('Descripcion', blank=False, max_length=180)
    fecha_creacion_servicio = models.DateField()
    fecha_modificacion_servicio = models.DateField()
    status_servicio = models.CharField('status', blank=False, max_length=1)

    def __str__(self):
        return self.nombre_servicio

class Sucursales(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField('Nombre', blank=False, max_length=180)
    descripcion_sucursal = models.CharField('Descripcion', blank=False, max_length=300)
    telefono_sucursal = models.CharField('Telefono', blank=False,max_length=10)
    servicio = models.ManyToManyField(Servicios, blank=True)
    fecha_creacion_sucursal = models.DateField()
    fecha_modificacion_sucursal = models.DateField()
    status_sucursal = models.CharField('status', blank=False, max_length=1)

    def __str__(self):
        return self.nombre_sucursal

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo_libro = models.CharField('Nombres', blank=False, max_length=80)
    no_paginas_libro = models.IntegerField('Paginas')
    fecha_creacion_libro = models.DateField()
    fecha_modificacion_libro = models.DateField()
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    sucursal = models.ManyToManyField(Sucursales,blank=True)
    status_libro = models.CharField('status',blank=False, max_length=1)

    def __str__(self):
        return self.titulo_libro

class Revista(models.Model):
    id_revista = models.AutoField(primary_key=True)
    titulo_revista = models.CharField('Nombres', blank=False, max_length=80)
    no_paginas_revista = models.IntegerField('Paginas')
    fecha_creacion_revista = models.DateField()
    fecha_modificacion_revista = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sucursal = models.ManyToManyField(Sucursales,blank=True)
    status_revista = models.CharField('status', blank=False, max_length=1)

    def __str__(self):
        return self.titulo_revista

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField('Username', blank=False, max_length=80)
    password = models.CharField('Paswword', blank=False, max_length=80)
    status = models.CharField('Status', blank=True, max_length=1)