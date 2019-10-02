from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django import  forms
from django.template.loader import get_template

from .util import render_to_pdf
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from django.views.generic import(
    View,
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
)

from .models import *
class sesion:
    sesion=False
    def setsesion(self,valor):
        self.sesion = valor
    def getsesion(self):
        return self.sesion

class opcionesReportesAutores(ListView):
    template_name = "biblioteca/opciones-reportes-autores.html"

    def get_queryset(self):
        lista = Libro.objects.all()
        lista2 = Autor.objects.order_by("nacionalidad_autor").distinct("nacionalidad_autor")

        return lista, lista2

    context_object_name = "l"

class reporteAutoresLibro(ListView):

    def get(self, request, *args, **kwargs):
        template = get_template("biblioteca/reporte-autores-libro.html")
        id = self.kwargs["pk"]
        l = Libro.objects.filter(
            id_libro=id
        )
        l2 = Autor.objects.all()
        params = {
            'l': l,
            'l2': l2

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-autores-libro.html', params)
        return HttpResponse(pdf, content_type='application/pdf')

class CantidadAutor_libros(ListView):
    template_name = "biblioteca/reporte-cantidad-libros-autor.html"

    def get_queryset(self):
        id = self.kwargs["pk"]

        lista = Libro.objects.filter(
            autor=id
        ).values("autor").annotate(total=Count("autor"))

        lista2 = Autor.objects.all()

        return lista, lista2

    context_object_name = "l"

class ListaAutores(ListView):
    template_name = "biblioteca/Lista-autores.html"
    model = Autor
    context_object_name = "l"
    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        print(username)
        l = Autor.objects.order_by("id_autor")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/Lista-autores.html')
                    params = {
                        'l': l,
                        's': s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/metodopost.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/metodopost.html')
            html = template.render(params)
            return HttpResponse(html)


class lista(ListView):

    def get(self, request, *args, **kwargs):

        template = get_template("biblioteca/L.html")
        l = Autor.objects.all()
        l2 = Libro.objects.all()
        params = {
            'l':l,
            'l2':l2

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/L.html',params)
        return HttpResponse(pdf, content_type='application/pdf')

class CantidadCategoria_libros(ListView):

    def get(self, request, *args, **kwargs):

        template = get_template("biblioteca/reporte-cantidad-libros-categoria-pdf.html")
        id = self.kwargs["pk"]
        l = Libro.objects.filter(
            categoria=id
        ).values("categoria").annotate(total=Count("categoria"))
        l2 = Libro.objects.filter(
            categoria=id
        ).order_by("id_libro")
        params = {
            'l':l,
            'l2':l2

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-cantidad-libros-categoria-pdf.html',params)
        return HttpResponse(pdf, content_type='application/pdf')


class CantidadAutor_libros_pdf(ListView):



    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        template = get_template("biblioteca/reporte-cantidad-libros-autor-pdf.html")
        l = Libro.objects.filter(
            autor=id
        ).values("autor").annotate(total=Count("autor"))
        l2 = Libro.objects.filter(
            autor=id
        )
        params = {
            'l':l,
            'l2':l2

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-cantidad-libros-autor-pdf.html',params)
        return HttpResponse(pdf, content_type='application/pdf')

class CantidadAutor_nacionalidad_pdf(ListView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        template = get_template("biblioteca/reporte-autores-nacionalidad-pdf.html")
        l = Autor.objects.filter(
            nacionalidad_autor=id
        ).values("nacionalidad_autor").annotate(total=Count("nacionalidad_autor"))
        l2 = Autor.objects.all(

        )
        params = {
            'l':l,
            'l2':l2
        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-autores-nacionalidad-pdf.html',params)
        return HttpResponse(pdf, content_type='application/pdf')


class ListaLibros(ListView):
    template_name = "biblioteca/Lista-libros.html"
    model = Libro
    context_object_name = "l"
    def get(self, request, *args, **kwargs):
        username = self.kwargs["un"]
        print(username)
        l = Libro.objects.order_by("id_libro")

        s = Usuario.objects.filter(
            username = username
        )

        if s:
            for a in s:
                if a.status=='A':
                    template = get_template('biblioteca/Lista-libros.html')
                    params = {
                    'l':l,
                    's':s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/metodopost.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado':"error"}
            params = {
                'l':l
            }
            template = get_template('biblioteca/metodopost.html')
            html = template.render(params)
            return HttpResponse(html)

class listaReportesLibrosAutores(ListView):
    template_name = "biblioteca/opciones-reportes-libros-autores.html"
    model = Autor
    context_object_name = "l"

class listaReportesLibrosCategorias(ListView):
    template_name = "biblioteca/opciones-reportes-libros-categorias.html"
    model = Categoria
    context_object_name = "l"


class Inicio(TemplateView):

    template_name = "biblioteca/inicio.html"




class script(TemplateView):
    template_name = "statics/jsAutores.js"

class comprobacion(TemplateView):

    def post(self, request, *args, **kwargs):


        if request.method == 'POST':

            nombre = request.POST['username']
            password = request.POST['password']
            print(nombre+" "+password)
            if nombre == 'axl' and password == '123':
                print("entro al if")
                sesion.setsesion(sesion,True)
                print(sesion.getsesion(sesion))
                template = get_template("biblioteca/inicio.html")
                html = template.render()
                return HttpResponse(html)
            else:
                sesion.setsesion(sesion,False)

                print(sesion.getsesion(sesion))
                template = get_template("biblioteca/metodopost.html")
                html = template.render()
                return HttpResponse(html)

class r(ListView):

    def post(self, request, *args, **kwargs):


            pk = request.POST["name"]
            fk = request.POST["n"]
            template = get_template("biblioteca/nuevo.html")
            print(pk)
            l = Libro.objects.all()
            params = {
                'l': pk,
                'l2': fk
            }
            html = template.render(params)

            return HttpResponse(html)

class addAutor(CreateView):
    template_name = "biblioteca/add-autor.html"
    model = Autor
    fields = ["nombre_autor", "apellidos_autor","nacionalidad_autor","fecha_creacion_autor","fecha_modificacion_autor","status_autor"]
    labels = {
        'titulo': 'Titulo',
        'no_paginas': 'Numero de Paginas',
        'fecha_modificacion': 'Fecha de modificacion',
        'autor': 'Autor',
    }
    widgets = {
        'titulo': forms.TextInput(),
        'no_paginas': forms.NumberInput(),
        'fecha_modificacion': forms.TextInput(),
        'autor': forms.TextInput(),
        'status': forms.TextInput(),
    }
    success_url = "/biblioteca/autores"

class editAutor(UpdateView):
    template_name = "biblioteca/edit-autor.html"
    model = Autor
    fields = ["nombre_autor", "apellidos_autor","nacionalidad_autor","fecha_creacion_autor","fecha_modificacion_autor","status_autor"]

    success_url = "/biblioteca/autores"

class deleteAutor(UpdateView):
    template_name = "base/delete-autor.html"
    model = Autor
    fields = ["nombre_autor", "apellidos_autor","nacionalidad_autor","fecha_creacion_autor","fecha_modificacion_autor","status_autor"]

    success_url = "/biblioteca/autores"



class editLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo_libro', 'no_paginas_libro','fecha_creacion_libro', 'fecha_modificacion_libro','autor','editorial','categoria','sucursal', 'status_libro']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

class editLibro(UpdateView):
    form_class = editLibroForm
    template_name = "biblioteca/edit-libro.html"
    model = Libro
    success_url = "/biblioteca/libros"




class deleteLibro(UpdateView):
    template_name = "base/delete-libro.html"
    model = Libro
    fields = ["titulo_libro", "no_paginas_libro","fecha_creacion_libro","fecha_modificacion_libro","autor","status_libro"]

    success_url = "/biblioteca/libros"


class addLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo_libro', 'no_paginas_libro', 'fecha_creacion_libro', 'fecha_modificacion_libro', 'autor', 'categoria','editorial','sucursal', 'status_libro']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

class addLibro(CreateView):
    form_class = addLibroForm
    template_name = "biblioteca/add-libro.html"
    model = Libro
    success_url = "/biblioteca/libros"

class registro(TemplateView):

    template_name = "biblioteca/metodopost.html"




class errorsesion(ListView):


    def get(self, request, *args, **kwargs):

        id = request.GET["username"]
        contrasenia = request.GET["password"]

        l = Usuario.objects.filter(
            username=id,
            password=contrasenia
        )
        if l:
            s = Usuario.objects.filter(
                username=id,
            password=contrasenia
            ).update(
                status="A"
            )
            template = get_template('biblioteca/inicio.html')
            params = {
                'l':l
            }
            html = template.render(params)
            return HttpResponse(html)
        else:
            l = {'estado':"error"}
            params = {
                'l':l
            }
            template = get_template('biblioteca/metodopost.html')
            html = template.render(params)
            return HttpResponse(html)

class errorsesion2(ListView):


    def get(self, request, *args, **kwargs):
        id = self.kwargs["cs"]
        s = Usuario.objects.filter(
            username=id
        ).update(
            status="B"
        )
        template = get_template('biblioteca/metodopost.html')
        params = {
            'l':s
        }
        html = template.render()
        return HttpResponse(html)








#-------------------------------------------------------------------Nuevos CRUD-------------------------------------------------------------------

#---Categoria---
class addCategoria(CreateView):
    template_name = "biblioteca/add-categoria.html"
    model = Categoria
    fields = ["nombre_categoria","descripcion_categoria","fecha_creacion_categoria","fecha_modificacion_categoria","status_categoria"]
    success_url = "/biblioteca/categorias"

class ListaCategorias(ListView):
    template_name = "biblioteca/Lista-Categorias.html"
    model = Categoria
    context_object_name = "l"
    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        print(username)
        l = Categoria.objects.order_by("id_categoria")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/Lista-Categorias.html')
                    params = {
                        'l': l,
                        's': s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/metodopost.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/metodopost.html')
            html = template.render(params)
            return HttpResponse(html)

class editCategoria(UpdateView):
    template_name = "biblioteca/edit-categoria.html"
    model = Categoria
    fields = ["nombre_categoria", "descripcion_categoria","fecha_creacion_categoria","fecha_modificacion_categoria","status_categoria"]

    success_url = "/biblioteca/categorias"

class deleteCategoria(UpdateView):
    template_name = "base/delete-categoria.html"
    model = Categoria
    fields = ["nombre_categoria", "descripcion_categoria","fecha_creacion_categoria","fecha_modificacion_categoria","status_categoria"]
    success_url = "/biblioteca/categorias"

class buscarCategoria(ListView):
    template_name = "biblioteca/buscar-categoria.html"

    context_object_name = "l"

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs["pk"]
        # filtar los libros
        lista = Categoria.objects.filter(
            nombre_categoria=id
        )
        # DEvolver el resultado o la lista
        return lista
#---Categoria---

# ---Editorial---
class addEditorial(CreateView):
    template_name = "biblioteca/add-editorial.html"
    model = Editorial
    fields = ["nombre_editorial", "pais_editorial", "fecha_creacion_editorial", "fecha_modificacion_editorial", "status_editorial"]
    success_url = "/biblioteca/editoriales"


class ListaEditoriales(ListView):
    template_name = "biblioteca/Lista-editoriales.html"
    model = Editorial
    context_object_name = "l"

class editEditorial(UpdateView):
    template_name = "biblioteca/edit-editorial.html"
    model = Editorial
    fields = ["nombre_editorial", "pais_editorial","fecha_creacion_editorial","fecha_modificacion_editorial","status_editorial"]

    success_url = "/biblioteca/editoriales"

class deleteEditorial(UpdateView):
    template_name = "base/delete-editorial.html"
    model = Editorial
    fields = ["nombre_editorial", "pais_editorial", "fecha_creacion_editorial", "fecha_modificacion_editorial", "status_editorial"]
    success_url = "/biblioteca/editoriales"


class buscarEditorial(ListView):
    template_name = "biblioteca/buscar-editorial.html"

    context_object_name = "l"

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs["pk"]
        # filtar los libros
        lista = Editorial.objects.filter(
            nombre_editorial=id
        )
        # DEvolver el resultado o la lista
        return lista


# ---Editorial---

# ---Revista---
class addRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ['titulo_revista', 'no_paginas_revista','fecha_creacion_revista', 'fecha_modificacion_revista','categoria','sucursal', 'status_revista']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

class addRevista(CreateView):
    form_class = addRevistaForm
    template_name = "biblioteca/add-revista.html"
    model = Revista
    success_url = "/biblioteca/revistas"


class ListaRevistas(ListView):
    template_name = "biblioteca/Lista-revistas.html"
    model = Revista
    context_object_name = "l"
    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        print(username)
        l = Revista.objects.order_by("id_revista")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/Lista-revistas.html')
                    params = {
                        'l': l,
                        's': s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/metodopost.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/metodopost.html')
            html = template.render(params)
            return HttpResponse(html)

class editRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ['titulo_revista', 'no_paginas_revista','fecha_creacion_revista', 'fecha_modificacion_revista','categoria','sucursal', 'status_revista']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

class editRevista(UpdateView):
    form_class = editRevistaForm
    template_name = "biblioteca/edit-revista.html"
    model = Libro
    success_url = "/biblioteca/revistas"

class deleteRevista(UpdateView):
    template_name = "base/delete-revista.html"
    model = Revista
    fields = ["titulo_revista", "no_paginas_revista", "fecha_creacion_revista", "fecha_modificacion_revista","categoria", "status_revista"]
    success_url = "/biblioteca/revistas"


class buscarRevista(ListView):
    template_name = "biblioteca/buscar-revista.html"

    context_object_name = "l"

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs["pk"]
        # filtar los libros
        lista = Revista.objects.filter(
            titulo_revista=id
        )
        # DEvolver el resultado o la lista
        return lista


# ---Revista---

# ---sucarsal---

class addSucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = ['nombre_sucursal', 'descripcion_sucursal', 'telefono_sucursal', 'servicio', 'fecha_creacion_sucursal', 'fecha_modificacion_sucursal', 'status_sucursal']
        widgets = {
            'servicio': forms.CheckboxSelectMultiple()
        }

class addSucursal(CreateView):
    form_class = addSucursalForm
    template_name = "biblioteca/add-sucursal.html"
    model = Sucursales
    success_url = "/biblioteca/sucursales"





class ListaSucursales(ListView):
    template_name = "biblioteca/Lista-sucursales.html"
    model = Sucursales
    context_object_name = "l"
    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        print(username)
        l = Sucursales.objects.order_by("id_sucursal")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/Lista-sucursales.html')
                    params = {
                        'l': l,
                        's': s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/metodopost.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/metodopost.html')
            html = template.render(params)
            return HttpResponse(html)

class editSucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = ['nombre_sucursal', 'descripcion_sucursal', 'telefono_sucursal', 'servicio', 'fecha_creacion_sucursal', 'fecha_modificacion_sucursal', 'status_sucursal']
        widgets = {
            'servicio': forms.CheckboxSelectMultiple()
        }

class editSucursal(UpdateView):
    form_class = addSucursalForm
    model = Sucursales
    success_url = "/biblioteca/sucursales"



class deleteSucursal(UpdateView):
    template_name = "base/delete-sucursal.html"
    model = Sucursales
    fields = ["nombre_sucursal", "descripcion_sucursal","telefono_sucursal", "fecha_creacion_sucursal", "fecha_modificacion_sucursal", "status_sucural"]
    success_url = "/biblioteca/sucursales"


class buscarSucursal(ListView):
    template_name = "biblioteca/buscar-sucursal.html"

    context_object_name = "l"

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs["pk"]
        # filtar los libros
        lista = Sucursales.objects.filter(
            nombre_sucursal=id
        )
        # DEvolver el resultado o la lista
        return lista


# ---Sucursal---

#---Servicio---
class addServicio(CreateView):
    template_name = "biblioteca/add-servicio.html"
    model = Servicios
    fields = ["nombre_servicio", "descripcion_servicio", "fecha_creacion_servicio", "fecha_modificacion_servicio", "status_servicio"]
    success_url = "/biblioteca/servicios"


class ListaServicios(ListView):
    template_name = "biblioteca/Lista-servicios.html"
    model = Servicios
    context_object_name = "l"
    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        print(username)
        l = Servicios.objects.order_by("id_servicio")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/Lista-servicios.html')
                    params = {
                        'l': l,
                        's': s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/metodopost.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/metodopost.html')
            html = template.render(params)
            return HttpResponse(html)

class editServicio(UpdateView):
    template_name = "biblioteca/edit-servicio.html"
    model = Servicios
    fields = ["nombre_servicio", "descripcion_servicio","fecha_creacion_servicio","fecha_modificacion_servicio","status_servicio"]

    success_url = "/biblioteca/servicios"

class deleteServicio(UpdateView):
    template_name = "base/delete-servicio.html"
    model = Servicios
    fields = ["nombre_servicio", "descripcion_servicio","fecha_creacion_servicio", "fecha_modificacion_servicio", "status_servicio"]
    success_url = "/biblioteca/servicios"


class buscarServicio(ListView):
    template_name = "biblioteca/buscar-servicio.html"

    context_object_name = "l"

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs["pk"]
        # filtar los libros
        lista = Servicios.objects.filter(
            nombre_servicio=id
        )
        # DEvolver el resultado o la lista
        return lista

#---Servicio---
#---Usuarios---

class addUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'fecha_creacion', 'fecha_modificacion', 'status']
        widgets = {
            'password': forms.PasswordInput()
        }

class addUsuario(CreateView):
    form_class = addUsuarioForm
    template_name = "biblioteca/add-usuario.html"
    model = Usuario
    success_url = "/biblioteca/"
#---Usuarios---
#-------------------------------------------------------------------------------------------------------------------------------------------------

class buscarLibro(ListView):
    template_name = "biblioteca/buscar-libros.html"

    context_object_name = "l"

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs["pk"]
        # filtar los libros
        lista = Libro.objects.filter(
            titulo_libro=id
        )
        # DEvolver el resultado o la lista
        return lista

class buscarAutor(ListView):
    template_name = "biblioteca/buscar-Autor.html"

    context_object_name = "l"


    def get_queryset(self):
        # identificar el autor
        id = self.kwargs["pk"]
        # filtar los libros
        lista = Autor.objects.filter(
            nombre_autor=id
        )

        # DEvolver el resultado o la lista
        return lista

class rangoflibros(ListView):

    def get(self, request, *args, **kwargs):
        template = get_template("biblioteca/reporte-fecha-libros.html")
        fi = self.kwargs["pk"]
        ff = self.kwargs["fk"]
        rango = fi+" y "+ff
        fecha = [rango]

        l = Libro.objects.filter(
            fecha_creacion_libro__range=[str(fi), str(ff)]
        )

        params = {
            'l': l,
            'l2': rango

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-fecha-libros.html', params)
        return HttpResponse(pdf, content_type='application/pdf')