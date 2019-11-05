from django.db import models
import datetime

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
    vistas = models.IntegerField('vistas', blank=True)
    costo = models.IntegerField('costo', blank=False, default=0)
    sinopsis = models.CharField('sinopsis', blank=False, default='o', max_length=1000)
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
    costo = models.IntegerField('costo', blank=False, default=0)
    status_revista = models.CharField('status', blank=False, max_length=1)

    def __str__(self):
        return self.titulo_revista

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField('Username', blank=False, max_length=80)
    password = models.CharField('Paswword', blank=False, max_length=80)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    status = models.CharField('Status', blank=True, max_length=1)

    def __str__(self):
        return self.username


class codigoAdmin(models.Model):
    id_codigo = models.AutoField(primary_key=True)
    codigo = models.CharField('codigo', blank=False, max_length=6)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class login(models.Model):
    id_login = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', blank=False, max_length=20)
    apellido_paterno = models.CharField('apellido_paterno', blank=False, max_length=15)
    apellido_materno = models.CharField('apellido_materno', blank=True, max_length=15)
    email = models.EmailField
    username = models.CharField('username', blank=False, max_length=20)
    password = models.CharField('password', blank=False, max_length=20)
    saldo = models.IntegerField('saldo', blank=False, default=0)
    fecha_creacion = models.DateField(default=datetime.date.today)
    fecha_modificacion = models.DateField(default=datetime.date.today)
    status = models.CharField('status', blank=True, max_length=1, default='B')

class favoritos(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, blank=False, on_delete=models.CASCADE)
    login = models.ForeignKey(login, blank=False, on_delete=models.CASCADE)

class compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, blank=False, on_delete=models.CASCADE)
    login = models.ForeignKey(login, blank=False, on_delete=models.CASCADE)

class compraR(models.Model):
    id_compra = models.AutoField(primary_key=True)
    revista = models.ForeignKey(Revista, blank=False, on_delete=models.CASCADE)
    login = models.ForeignKey(login, blank=False, on_delete=models.CASCADE)

class comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    texto = models.CharField('texto', blank=False, max_length=1000)
    login = models.ForeignKey(login, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)