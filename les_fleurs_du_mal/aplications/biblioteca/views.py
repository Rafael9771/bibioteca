from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django import  forms
from django.template.loader import get_template
from django.urls import reverse_lazy
from django import template
from .util import render_to_pdf
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render
from django import template
from django.contrib import messages
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

class verlibros(ListView):

    def get(self, request, *args, **kwargs):
        l = Libro.objects.filter(
            status_libro="A"
        ).order_by('-vistas')
        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')
        template = get_template('biblioteca/libros.html')
        params={
            'l':l,
            'c':c
        }
        html = template.render(params)
        return HttpResponse(html)



class mostrarlibro(ListView):


    def get(self, request, *args, **kwargs):
        libro = self.kwargs["lb"]
        v = self.kwargs["v"]
        s = Libro.objects.filter(titulo_libro=libro)
        l = Libro.objects.filter(
            titulo_libro=libro
        ).update(vistas=int(v)+1)

        template=get_template('biblioteca/libro.html')
        params={
            'l':s
        }
        html = template.render(params)
        return HttpResponse(html)

class opcionesReportesAutores(ListView):

    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        l2 = Autor.objects.order_by("nacionalidad_autor").distinct("nacionalidad_autor")
        l = Libro.objects.all()

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/opciones-reportes-autores.html')
                    params = {
                        'l': l,
                        'l2':l2,
                        's': s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)


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
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
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

class CantidadCategoria_revistas(ListView):

    def get(self, request, *args, **kwargs):

        template = get_template("biblioteca/reporte-cantidad-revistas-categoria-pdf.html")
        id = self.kwargs["pk"]
        l = Revista.objects.filter(
            categoria=id
        ).values("categoria").annotate(total=Count("categoria"))

        l2 = Revista.objects.filter(
            categoria=id
        ).order_by("id_revista")
        params = {
            'l':l,
            'l2':l2

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-cantidad-revistas-categoria-pdf.html',params)
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
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado':"error"}
            params = {
                'l':l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

class listaReportesLibrosAutores(ListView):


    def get(self, request, *args, **kwargs):
        username = self.kwargs["un"]

        l = Revista.objects.filter(status_revista='A')

        s = Usuario.objects.filter(
            username=username
        )

        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/opciones-reportes-revista.html')
                    params = {
                        'l': l,
                        's': s,
                        'c':c
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

class listaReportesLibrosCategorias(ListView):


    def get(self, request, *args, **kwargs):
        username = self.kwargs["un"]

        l = Autor.objects.filter(status_autor='A')

        s = Usuario.objects.filter(
            username=username
        )

        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/opciones-reportes-libros-categorias.html')
                    params = {
                        'l': l,
                        's': s,
                        'c':c
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

class Inicio(ListView):


    def get(self, request, *args, **kwargs):
        username = self.kwargs["un"]
        print(username)
        l = Libro.objects.filter(
            status_libro="A"
        ).order_by('-vistas')

        s = Usuario.objects.filter(
            username=username
        )

        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/inicio2.html')
                    params = {
                        'l': l,
                        's': s,
                        'c':c
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)



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
                template = get_template("biblioteca/index.html")
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

class addAutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre_autor", "apellidos_autor", "nacionalidad_autor", "fecha_creacion_autor",
                  "fecha_modificacion_autor", "status_autor"]
        labels = {
            'titulo': 'Titulo',
            'no_paginas': 'Numero de Paginas',
            'fecha_modificacion': 'Fecha de modificacion',
            'autor': 'Autor',
        }

class addAutor(CreateView):

    un = ''
    def get(self, request, *args, **kwargs):
        un = self.kwargs["un"]
        usuario = Usuario.objects.filter(
            username=un
        )
        if usuario:
            for a in usuario:
                if a.status=='A':
                    context = {'form': addAutorForm()}
                    return render(request, 'biblioteca/add-autor.html', context)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)
        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            return render(request, 'biblioteca/index.html', params)


    def post(self, request, *args, **kwargs):
        form = addAutorForm(request.POST)

        nombre = request.POST['nombre_autor']
        apellidos = request.POST['apellidos_autor']

        user = Autor.objects.filter(nombre_autor=nombre,apellidos_autor=apellidos).exists()
        if user:
            r = self.kwargs["un"]
            messages.error(request,'Error el autor ya exixte')
            return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_autores', kwargs={'un': r}))


        else:
            if form.is_valid():
                book = form.save()
                book.save()
                r=self.kwargs["un"]

                return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_autores',kwargs={'un':r}))

class deleteAutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre_autor", "apellidos_autor", "nacionalidad_autor", "fecha_creacion_autor",
                  "fecha_modificacion_autor", "status_autor"]

class editAutor(UpdateView):

    form_class = deleteAutorForm
    template_name = 'biblioteca/edit-autor.html'
    model = Autor
    def get_success_url(self, **kwargs):
        username=self.kwargs["un"]
        l = Usuario.objects.filter(
            username=username
        )
        if l:
            for a in l:
                if a.status=='A':
                    return reverse_lazy('biblioteca_app:lista_autores',kwargs={'un':username})
                else:
                    return reverse_lazy('biblioteca_app:sd')

        else:
            return reverse_lazy('biblioteca_app:sd')








class deleteAutor(UpdateView):
    template_name = "biblioteca/delete-autor.html"
    model = Autor
    form_class = deleteAutorForm

    def get_success_url(self,**kwargs):
        r=self.kwargs["un"]
        return reverse_lazy('biblioteca_app:lista_autores',kwargs={'un':r})


class deleteLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo_libro", "no_paginas_libro","fecha_creacion_libro","fecha_modificacion_libro","autor","status_libro"]


class editLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo_libro', 'no_paginas_libro','fecha_creacion_libro', 'fecha_modificacion_libro','autor','editorial','categoria','sucursal','costo', 'status_libro']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

class editLibro(UpdateView):
    form_class = editLibroForm
    template_name = "biblioteca/edit-libro.html"
    model = Libro

    def get_success_url(self, **kwargs):
        username=self.kwargs["un"]
        l = Usuario.objects.filter(
            username=username
        )
        if l:
            for a in l:
                if a.status=='A':
                    return reverse_lazy('biblioteca_app:lista_libros',kwargs={'un':username})
                else:
                    return reverse_lazy('biblioteca_app:sd')

        else:
            return reverse_lazy('biblioteca_app:sd')




class deleteLibro(UpdateView):
    template_name = "biblioteca/delete-libro.html"
    model = Libro
    form_class = deleteLibroForm
    def get_success_url(self, **kwargs):
        r = self.kwargs["un"]
        return reverse_lazy('biblioteca_app:lista_libros', kwargs={'un': r})

class addLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo_libro', 'no_paginas_libro', 'fecha_creacion_libro', 'fecha_modificacion_libro', 'autor', 'categoria','editorial','sucursal', 'status_libro','vistas','costo']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(addLibroForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(status_categoria='A')
        self.fields['autor'].queryset = Autor.objects.filter(status_autor='A')
        self.fields['editorial'].queryset = Editorial.objects.filter(status_editorial='A')
        self.fields['sucursal'].queryset = Sucursales.objects.filter(status_sucursal='A')

class addLibro(CreateView):

    def get(self, request, *args, **kwargs):
        un = self.kwargs["un"]
        usuario = Usuario.objects.filter(
            username=un
        )
        if usuario:
            for a in usuario:
                if a.status == 'A':
                    context = {'form': addLibroForm()}
                    return render(request, 'biblioteca/add-libro.html', context)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)
        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            return render(request, 'biblioteca/index.html', params)

    def post(self, request, *args, **kwargs):
        form = addLibroForm(request.POST)
        nombre = request.POST['titulo_libro']
        user = Libro.objects.filter(titulo_libro=nombre).exists()
        if user:
            r = self.kwargs["un"]
            messages.error(request, 'Error el autor ya exixte')
            return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_libros', kwargs={'un': r}))


        else:
            if form.is_valid():
                book = form.save()
                book.save()
                r = self.kwargs["un"]

                return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_libros', kwargs={'un': r}))


class errorCA(TemplateView):
    template_name = 'biblioteca/errorAdmin.html'

class addLoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ['nombre','apellido_paterno','apellido_materno','username', 'password', 'fecha_creacion', 'fecha_modificacion', 'status']
        widgets = {
            'password': forms.PasswordInput(),

        }





class addLogin(CreateView):


    def get(self, request, *args, **kwargs):

        context = {'form': addLoginForm}
        return render(request, 'biblioteca/add-login.html', context)




    def post(self, request, *args, **kwargs):
        form = addLoginForm(request.POST)
        nombre = request.POST['nombre']
        apellidoP = request.POST['apellido_paterno']
        apellidoM = request.POST['apellido_materno']
        nickname = request.POST['username']
        contrasenia = request.POST['password']
        if len(contrasenia) > 8:

            user = login.objects.filter(username=nickname, nombre=nombre, apellido_paterno=apellidoP, apellido_materno=apellidoM).exists()
            if user:
                s = {'ErrorLoginExist':'Error el usuario ya existe'}
                params = {'ErrorLoginExist':s}
                template = get_template('biblioteca/add-login.html')
                html = template.render(params)
                return HttpResponse(html)



            else:
                if form.is_valid():
                    book = form.save()
                    book.save()


                    return HttpResponseRedirect(reverse_lazy('biblioteca_app:sesionLogin', kwargs={'us': nickname}))
        else:
            s = {'errorTamanioContra': 'La contraseña debe de ser de almenos 8 caracteres'}
            params = {
                'errorTamanioContra': s
            }
            template = get_template('biblioteca/add-login.html')
            html = template.render(params)
            return HttpResponse(html)



class sesionLogin(ListView):

    def get(self, request, *args, **kwargs):
        usuario = self.kwargs["us"]
        l = Libro.objects.filter(
            status_libro="A"
        ).order_by('-vistas')
        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')

        us = login.objects.filter(
            username=usuario,status='A'
        )
        if us:
            params = {
                'l':l,
                'c':c,
                'us':us
            }
            template = get_template('biblioteca/sesionLogin.html')
            html = template.render(params)
            return HttpResponse(html)
        else:
            s = {'errorLoginStatus':'este usuario no ha iniciado sesion'}
            params = {
                'l': l,
                'c': c,
                'errorLoginStatus': s
            }
            template = get_template('biblioteca/sesionLogin.html')
            html = template.render(params)
            return HttpResponse(html)

class inicioLogin(ListView):

    def get(self, request, *args, **kwargs):
        l = Libro.objects.filter(
            status_libro="A"
        ).order_by('-vistas')
        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')


        template = get_template('biblioteca/inicioLogin.html')
        params = {
            'l': l,
            'c': c
        }
        html = template.render(params)
        return HttpResponse(html)


class errorLogin(ListView):

    def get(self, request, *args, **kwargs):
        usuario = request.GET["username"]
        contrasenia = request.GET["password"]
        l = Libro.objects.filter(
            status_libro="A"
        ).order_by('-vistas')
        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')

        us =login.objects.filter(
            username = usuario,
            password = contrasenia
        )

        if us:
            s = login.objects.filter(
                username=usuario,
                password=contrasenia
            ).update(
                status="A"
            )
            template = get_template('biblioteca/sesionLogin.html')#Falta hacer el inicio con el login echo
            params = {
                'l':l,
                'c':c,
                'us':us
            }

            html = template.render(params)
            return HttpResponse(html)
        else:
            s = {'estado': "error"}
            template = get_template('biblioteca/sesionLogin.html')
            params = {
                'l': l,
                'c': c,
                'errorLogin':s
            }

            html = template.render(params)
            return HttpResponse(html)



class registro(ListView):

    def get(self, request, *args, **kwargs):
        l = Libro.objects.filter(
            status_libro="A"
        ).order_by('-vistas')
        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')
        codigoAmin = self.kwargs['ca']

        ca = codigoAdmin.objects.filter(codigo=codigoAmin)
        if ca:
            template = get_template('biblioteca/index.html')
            params = {
                'l': l,
                'c': c
            }
            html = template.render(params)
            return HttpResponse(html)
        else:
            template = get_template('biblioteca/errorAdmin.html')
            html = template.render()
            return HttpResponse(html)





class errorsesion(ListView):


    def get(self, request, *args, **kwargs):

        id = request.GET["username"]
        contrasenia = request.GET["password"]
        codigoAd = request.GET['codigoAdmin']
        print(id+" "+contrasenia+" "+codigoAd)
        l2 = Libro.objects.filter(
            status_libro="A"
        ).order_by('-vistas')
        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')
        us = Usuario.objects.filter(
            username=id,
            password=contrasenia
        )

        if us:

            for a in us:
                l = codigoAdmin.objects.filter(
                    codigo=codigoAd,usuario=a.id_usuario
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
                    'l': us,
                    'l2': l2,
                    'c': c
                }
                html = template.render(params)
                return HttpResponse(html)
            else:
                error = {'estado': "usuario no iniciado",'codigoAdmin':codigoAd}

                l2 = Libro.objects.filter(
                    status_libro="A"
                ).order_by('-vistas')
                c = Categoria.objects.filter(
                    status_categoria="A"
                ).order_by('nombre_categoria')
                s = {'estado': "error"}
                l = Libro.objects.filter(status_libro="A")
                params = {
                    's': s,
                    'l': l,
                    'l2': l2,
                    'c': c,
                    'errorSesionCodigo': error
                }
                template = get_template('biblioteca/index.html')
                html = template.render(params)
                return HttpResponseRedirect(reverse_lazy('biblioteca_app:sd', kwargs={'ca': codigoAd}))
        else:
            error = {'estado': "usuario no iniciado",'codigoAdmin':codigoAd}

            l2 = Libro.objects.filter(
                status_libro="A"
            ).order_by('-vistas')
            c = Categoria.objects.filter(
                status_categoria="A"
            ).order_by('nombre_categoria')
            s = {'estado': "error"}
            l = Libro.objects.filter(status_libro="A")
            params = {
                's': s,
                'l': l,
                'l2': l2,
                'c': c,
                'errorSesion': error
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponseRedirect(reverse_lazy('biblioteca_app:sd', kwargs={'ca': codigoAd}))

class errorsesion2(ListView):


    def get(self, request, *args, **kwargs):
        id = self.kwargs["cs"]
        s = Usuario.objects.filter(
            username=id
        ).update(
            status="B"
        )
        s2 = Usuario.objects.filter(
            username=id
        )
        c = Categoria.objects.filter(
            status_categoria="A"
        ).order_by('nombre_categoria')
        l = Libro.objects.filter(status_libro="A")
        template = get_template('biblioteca/index.html')
        params = {
            's':s2,
            'l':l,
            'c':c
        }
        html = template.render(params)
        return HttpResponse(html)








#-------------------------------------------------------------------Nuevos CRUD-------------------------------------------------------------------

#---Categoria---
class addCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre_categoria","descripcion_categoria","fecha_creacion_categoria","fecha_modificacion_categoria","status_categoria"]



class addCategoria(CreateView):

    def get(self, request, *args, **kwargs):
        un = self.kwargs["un"]
        usuario = Usuario.objects.filter(
            username=un
        )
        if usuario:
            for a in usuario:
                if a.status == 'A':
                    context = {'form': addCategoriaForm()}
                    return render(request, 'biblioteca/add-categoria.html', context)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)
        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            return render(request, 'biblioteca/index.html', params)

    def post(self, request, *args, **kwargs):
        form = addCategoriaForm(request.POST)

        nombre = request.POST['nombre_categoria']
        user = Categoria.objects.filter(nombre_categoria=nombre).exists()
        if user:
            r = self.kwargs["un"]
            messages.error(request, 'Error el autor ya exixte')
            return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_categorias', kwargs={'un': r}))

        else:
            if form.is_valid():
                book = form.save()
                book.save()
                r = self.kwargs["un"]

                return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_categorias', kwargs={'un': r}))


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
                        's': s,
                        'user':username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

class deleteCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre_categoria", "descripcion_categoria","fecha_creacion_categoria","fecha_modificacion_categoria","status_categoria"]

class editCategoria(UpdateView):
    template_name = "biblioteca/edit-categoria.html"
    model = Categoria
    form_class = deleteCategoriaForm

    def get_success_url(self, **kwargs):
        username=self.kwargs["un"]
        l = Usuario.objects.filter(
            username=username
        )
        if l:
            for a in l:
                if a.status=='A':
                    return reverse_lazy('biblioteca_app:lista_categorias',kwargs={'un':username})
                else:
                    return reverse_lazy('biblioteca_app:sd')

        else:
            return reverse_lazy('biblioteca_app:sd')







class deleteCategoria(UpdateView):
    template_name = "biblioteca/delete-categoria.html"
    model = Categoria
    form_class = deleteCategoriaForm

    def get_success_url(self, **kwargs):
        r = self.kwargs["un"]
        return reverse_lazy('biblioteca_app:lista_categorias', kwargs={'un': r})

class buscarCategoria(ListView):
    template_name = "biblioteca/buscar-categoria.html"
    model = Categoria
    context_object_name = "l"


    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        username = self.kwargs["un"]

        l = Categoria.objects.filter(nombre_categoria=id)

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/buscar-categoria.html')
                    params = {
                        'l': l
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)
#---Categoria---

# ---Editorial---
class addEditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ["nombre_editorial", "pais_editorial", "fecha_creacion_editorial", "fecha_modificacion_editorial", "status_editorial"]



class addEditorial(CreateView):
    un = ''
    def get(self, request, *args, **kwargs):
        un = self.kwargs["un"]
        usuario = Usuario.objects.filter(
            username=un
        )
        if usuario:
            for a in usuario:
                if a.status == 'A':
                    context = {'form': addEditorialForm()}
                    return render(request, 'biblioteca/add-editorial.html', context)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)
        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            return render(request, 'biblioteca/index.html', params)

    def post(self, request, *args, **kwargs):
        form = addEditorialForm(request.POST)
        nombre = request.POST['nombre_editorial']
        user = Editorial.objects.filter(nombre_editorial=nombre).exists()
        if user:
            r = self.kwargs["un"]
            messages.error(request, 'Error el autor ya exixte')
            return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_editoriales', kwargs={'un': r}))


        else:
            if form.is_valid():
                book = form.save()
                book.save()
                r = self.kwargs["un"]

                return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_editoriales', kwargs={'un': r}))



class ListaEditoriales(ListView):
    template_name = "biblioteca/Lista-editoriales.html"
    model = Editorial
    context_object_name = "l"

    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        print(username)
        l = Editorial.objects.order_by("id_editorial")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/Lista-editoriales.html')
                    params = {
                        'l': l,
                        's': s,
                        'user': username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)


class deleteEditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ["nombre_editorial", "pais_editorial", "fecha_creacion_editorial", "fecha_modificacion_editorial",
                  "status_editorial"]

class editEditorial(UpdateView):
    template_name = "biblioteca/edit-editorial.html"
    model = Editorial
    form_class = deleteEditorialForm

    def get_success_url(self, **kwargs):
        username=self.kwargs["un"]
        l = Usuario.objects.filter(
            username=username
        )
        if l:
            for a in l:
                if a.status=='A':
                    return reverse_lazy('biblioteca_app:lista_editoriales',kwargs={'un':username})
                else:
                    return reverse_lazy('biblioteca_app:sd')

        else:
            return reverse_lazy('biblioteca_app:sd')





class deleteEditorial(UpdateView):
    template_name = "base/delete-editorial.html"
    model = Editorial
    form_class = deleteEditorialForm

    def get_success_url(self, **kwargs):
        r = self.kwargs["un"]
        return reverse_lazy('biblioteca_app:lista_editoriales', kwargs={'un': r})

class buscarEditorial(ListView):
    template_name = "biblioteca/buscar-editorial.html"
    model = Editorial
    context_object_name = "l"

    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        username = self.kwargs["un"]

        l = Editorial.objects.filter(nombre_editorial=id).order_by("id_editorial")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/buscar-editorial.html')
                    params = {
                        'l': l,
                        's': s,
                        'user': username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)


# ---Editorial---

# ---Revista---
class addRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ['titulo_revista', 'no_paginas_revista','fecha_creacion_revista', 'fecha_modificacion_revista','categoria','sucursal','costo', 'status_revista']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

        def __init__(self, *args, **kwargs):
            super(addRevistaForm, self).__init__(*args, **kwargs)
            self.fields['categoria'].queryset = Categoria.objects.filter(status_categoria='A')
            self.fields['sucursal'].queryset = Sucursales.objects.filter(status_sucursal='A')



class addRevista(CreateView):
    form_class = addRevistaForm
    template_name = "biblioteca/add-revista.html"
    model = Revista
    success_url = "/biblioteca/revistas"

    def get(self, request, *args, **kwargs):
        un = self.kwargs["un"]
        usuario = Usuario.objects.filter(
            username=un
        )
        if usuario:
            for a in usuario:
                if a.status == 'A':
                    context = {'form': addRevistaForm()}
                    return render(request, 'biblioteca/add-revista.html', context)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)
        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            return render(request, 'biblioteca/index.html', params)

    def post(self, request, *args, **kwargs):
        form = addRevistaForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            r = self.kwargs["un"]

            return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_revistas', kwargs={'un': r}))



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
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

class editRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ['titulo_revista', 'no_paginas_revista','fecha_creacion_revista', 'fecha_modificacion_revista','categoria','sucursal','costo', 'status_revista']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple()
        }

class editRevista(UpdateView):
    form_class = editRevistaForm
    template_name = "biblioteca/edit-revista.html"
    model = Revista

    def get_success_url(self, **kwargs):
        username=self.kwargs["un"]
        l = Usuario.objects.filter(
            username=username
        )
        if l:
            for a in l:
                if a.status=='A':
                    return reverse_lazy('biblioteca_app:lista_revistas',kwargs={'un':username})
                else:
                    return reverse_lazy('biblioteca_app:sd')

        else:
            return reverse_lazy('biblioteca_app:sd')


class deleteRevistaForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = ["titulo_revista", "no_paginas_revista", "fecha_creacion_revista", "fecha_modificacion_revista",
                  "categoria", "status_revista"]




class deleteRevista(UpdateView):
    template_name = "biblioteca/delete-revista.html"
    model = Revista
    form_class = deleteRevistaForm

    def get_success_url(self, **kwargs):
        r = self.kwargs["un"]
        return reverse_lazy('biblioteca_app:lista_revistas', kwargs={'un': r})

class buscarRevista(ListView):
    template_name = "biblioteca/buscar-revista.html"
    model = Revista
    context_object_name = "l"


    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        username = self.kwargs["un"]

        l = Revista.objects.filter(titulo_revista=id).order_by("id_revista")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/buscar-revista.html')
                    params = {
                        'l': l,
                        's': s,
                        'user': username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)


# ---Revista---

# ---sucarsal---

class addSucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = ['nombre_sucursal', 'descripcion_sucursal', 'telefono_sucursal', 'servicio', 'fecha_creacion_sucursal', 'fecha_modificacion_sucursal', 'status_sucursal']
        widgets = {
            'servicio': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(addSucursalForm, self).__init__(*args, **kwargs)
        self.fields['servicio'].queryset = Servicios.objects.filter(status_servicio='A')



class addSucursal(CreateView):
    def get(self, request, *args, **kwargs):
        un = self.kwargs["un"]
        usuario = Usuario.objects.filter(
            username=un
        )
        if usuario:
            for a in usuario:
                if a.status == 'A':
                    context = {'form': addSucursalForm()}
                    return render(request, 'biblioteca/add-sucursal.html', context)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)
        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            return render(request, 'biblioteca/index.html', params)

    def post(self, request, *args, **kwargs):
        form = addSucursalForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            r = self.kwargs["un"]

            return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_sucursales', kwargs={'un': r}))


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
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
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
    template_name = 'biblioteca/edit-sucursal.html'
    def get_success_url(self, **kwargs):
        username=self.kwargs["un"]
        l = Usuario.objects.filter(
            username=username
        )
        if l:
            for a in l:
                if a.status=='A':
                    return reverse_lazy('biblioteca_app:lista_sucursales',kwargs={'un':username})
                else:
                    return reverse_lazy('biblioteca_app:sd')

        else:
            return reverse_lazy('biblioteca_app:sd')


class deleteSucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = ["nombre_sucursal", "descripcion_sucursal", "telefono_sucursal", "fecha_creacion_sucursal",
                  "fecha_modificacion_sucursal", "status_sucursal"]






class deleteSucursal(UpdateView):
    template_name = "biblioteca/delete-sucursal.html"
    model = Sucursales
    form_class = deleteSucursalForm
    def get_success_url(self, **kwargs):
        r = self.kwargs["un"]
        return reverse_lazy('biblioteca_app:lista_sucursales', kwargs={'un': r})

class buscarSucursal(ListView):
    template_name = "biblioteca/buscar-sucursal.html"
    model = Sucursales
    context_object_name = "l"

    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        username = self.kwargs["un"]

        l = Categoria.objects.filter(nombre_sucursal=id).order_by("id_sucursal")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/buscar-sucursal.html')
                    params = {
                        'l': l,
                        's': s,
                        'user': username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)


# ---Sucursal---

#---Servicio---
class addServicioForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ["nombre_servicio", "descripcion_servicio", "fecha_creacion_servicio", "fecha_modificacion_servicio", "status_servicio"]


class addServicio(CreateView):


    def get(self, request, *args, **kwargs):
        un = self.kwargs["un"]
        usuario = Usuario.objects.filter(
            username=un
        )
        if usuario:
            for a in usuario:
                if a.status == 'A':
                    context = {'form': addServicioForm()}
                    return render(request, 'biblioteca/add-servicio.html', context)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)
        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            return render(request, 'biblioteca/index.html', params)

    def post(self, request, *args, **kwargs):
        form = addServicioForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            r = self.kwargs["un"]

            return HttpResponseRedirect(reverse_lazy('biblioteca_app:lista_servicios', kwargs={'un': r}))




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
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

class deleteServicioForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ["nombre_servicio", "descripcion_servicio","fecha_creacion_servicio", "fecha_modificacion_servicio", "status_servicio"]

class editServicio(UpdateView):
    template_name = "biblioteca/edit-servicio.html"
    model = Servicios
    form_class = deleteServicioForm

    def get_success_url(self, **kwargs):
        username=self.kwargs["un"]
        l = Usuario.objects.filter(
            username=username
        )
        if l:
            for a in l:
                if a.status=='A':
                    return reverse_lazy('biblioteca_app:lista_servicios',kwargs={'un':username})
                else:
                    return reverse_lazy('biblioteca_app:sd')

        else:
            return reverse_lazy('biblioteca_app:sd')





class deleteServicio(UpdateView):
    template_name = "biblioteca/delete-servicio.html"
    model = Servicios
    form_class = deleteServicioForm

    def get_success_url(self, **kwargs):
        r = self.kwargs["un"]
        return reverse_lazy('biblioteca_app:lista_servicios', kwargs={'un': r})


class buscarServicio(ListView):
    template_name = "biblioteca/buscar-servicio.html"
    model = Servicios
    context_object_name = "l"

    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        username = self.kwargs["un"]

        l = Categoria.objects.filter(nombre_servicio=id).order_by("id_servicio")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/buscar-servicio.html')
                    params = {
                        'l': l,
                        's': s,
                        'user': username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

#---Servicio---
#---Usuarios---

class addUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'fecha_creacion', 'fecha_modificacion', 'status']
        widgets = {
            'password': forms.PasswordInput()
        }



class addUsuarioAdmin(CreateView):


    def get(self, request, *args, **kwargs):
        id = self.kwargs["ca"]
        username = self.kwargs["us"]
        print(id+" "+username)
        user = Usuario.objects.filter(username=username)
        for a in user:
            u = codigoAdmin.objects.filter(codigo=id,usuario=a.id_usuario)

        if u:

            for a in u:

                if a.usuario.status == 'A':

                    context = {'form': addUsuarioForm}
                    return render(request, 'biblioteca/add-usuario.html', context)
                else:
                    error = {'estado': "usuario no iniciado"}
                    params = {
                        'error': error
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

    def post(self, request, *args, **kwargs):
        form = addUsuarioForm(request.POST)
        nombre = request.POST['username']
        user = Usuario.objects.filter(username=nombre).exists()
        if user:

            messages.error(request, 'Error el autor ya exixte')
            return HttpResponseRedirect(reverse_lazy('biblioteca_app:index'))


        else:
            if form.is_valid():
                book = form.save()
                book.save()
                r = self.kwargs["us"]
                id = self.kwargs["ca"]

                return HttpResponseRedirect(reverse_lazy('biblioteca_app:codigoAdmin', kwargs={'us': r,'ca':id}))


class addcAdminForm(forms.ModelForm):
    class Meta:
        model = codigoAdmin
        fields = ['codigo', 'usuario']


class addCodigoAdmin(CreateView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs["ca"]
        username = self.kwargs["us"]
        print(id+" "+username)
        user = Usuario.objects.filter(username=username)
        for a in user:
            u = codigoAdmin.objects.filter(codigo=id,usuario=a.id_usuario)

        if u:

            for a in u:

                if a.usuario.status == 'A':

                    context = {'form': addcAdminForm}
                    return render(request, 'biblioteca/add-codigoAdmin.html', context)
                else:
                    error = {'estado': "usuario no iniciado"}
                    params = {
                        'error': error
                    }
                    template = get_template('biblioteca/index.html')
                    return render(request, 'biblioteca/index.html', params)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

    def post(self, request, *args, **kwargs):
        form = addcAdminForm(request.POST)
        nombre = request.POST['codigo']
        user = codigoAdmin.objects.filter(codigo=nombre).exists()
        if user:
            """r = self.kwargs["us"]
            messages.error(request, 'Error el autor ya exixte')
            return HttpResponseRedirect(reverse_lazy('biblioteca_app:index', kwargs={'un': r}))"""
            error = {'estado': "usuario no iniciado"}
            params = {
                'errorCodigoAdmin': error,
                'form': addcAdminForm
            }
            template = get_template('biblioteca/add-codigoAdmin.html')
            html = template.render(params)
            return render(request, 'biblioteca/add-codigoAdmin.html', params)



        else:
            if form.is_valid():
                book = form.save()
                book.save()
                r = self.kwargs["us"]

                return HttpResponseRedirect(reverse_lazy('biblioteca_app:index', kwargs={'un': r}))


class inicioAdmin():
    print("L")

#---Usuarios---
#-------------------------------------------------------------------------------------------------------------------------------------------------

class buscarLibro(ListView):
    template_name = "biblioteca/buscar-libros.html"
    model = Libro
    context_object_name = "l"

    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        username = self.kwargs["un"]

        l = Libro.objects.filter(titulo_libro=id).order_by("id_libro")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/buscar-libros.html')
                    params = {
                        'l': l,
                        's': s,
                        'user': username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)

class buscarAutor(ListView):
    template_name = "biblioteca/buscar-Autor.html"
    model = Autor
    context_object_name = "l"

    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        username = self.kwargs["un"]

        l = Autor.objects.filter(nombre_autor=id).order_by("id_autor")

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/buscar-Autor.html')
                    params = {
                        'l': l,
                        's': s,
                        'user': username
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)


class rangoflibros(ListView):

    def get(self, request, *args, **kwargs):
        template = get_template("biblioteca/reporte-fecha-libros.html")
        fi = self.kwargs["pk"]
        ff = self.kwargs["fk"]
        rango = fi+" y "+ff
        fecha = [rango]

        l = Libro.objects.filter(
            fecha_creacion_libro__range=[str(fi), str(ff)],
            status_libro='A'
        ).order_by('fecha_creacion_libro')

        params = {
            'l': l,
            'l2': rango

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-fecha-libros.html', params)
        return HttpResponse(pdf, content_type='application/pdf')


class rangofrevistas(ListView):

    def get(self, request, *args, **kwargs):
        template = get_template("biblioteca/reporte-fecha-revistas.html")
        fi = self.kwargs["pk"]
        ff = self.kwargs["fk"]
        rango = fi+" y "+ff
        fecha = [rango]

        l = Revista.objects.filter(
            fecha_creacion_revista__range=[str(fi), str(ff)],
            status_revista='A'
        ).order_by('fecha_creacion_revista')

        params = {
            'l': l,
            'l2': rango

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-fecha-revistas.html', params)
        return HttpResponse(pdf, content_type='application/pdf')


class CantidadSucursal_libros(ListView):

    def get(self, request, *args, **kwargs):

        template = get_template("biblioteca/reporte-cantidad-libros-sucursal-pdf.html")
        id = self.kwargs["pk"]
        l = Libro.objects.filter(
            sucursal=id
        ).values("sucursal").annotate(total=Count("sucursal"))
        l2 = Libro.objects.filter(
            sucursal=id,status_libro='A'
        ).order_by("id_libro")
        params = {
            'l':l,
            'l2':l2

        }
        html = template.render(params)
        pdf = render_to_pdf('biblioteca/reporte-cantidad-libros-sucursal-pdf.html',params)
        return HttpResponse(pdf, content_type='application/pdf')

class opcionesReportesSucursales(ListView):

    def get(self, request, *args, **kwargs):

        username = self.kwargs["un"]
        l2 = Sucursales.objects.order_by("nombre_sucursal").distinct("nombre_sucursal")
        l = Libro.objects.all()

        s = Usuario.objects.filter(
            username=username
        )

        if s:
            for a in s:
                if a.status == 'A':
                    template = get_template('biblioteca/opciones-reportes-Sucursales.html')
                    params = {
                        'l': l,
                        'l2':l2,
                        's': s
                    }
                    html = template.render(params)
                    return HttpResponse(html)
                else:
                    l = {'estado': "error"}
                    params = {
                        'l': l
                    }
                    template = get_template('biblioteca/index.html')
                    html = template.render(params)
                    return HttpResponse(html)

        else:
            l = {'estado': "error"}
            params = {
                'l': l
            }
            template = get_template('biblioteca/index.html')
            html = template.render(params)
            return HttpResponse(html)