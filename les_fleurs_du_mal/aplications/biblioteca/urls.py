from django.urls import path, re_path, include
from django.conf.urls import url, include

from . import views
from django.contrib.auth.views import LoginView ,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
from django.contrib.auth.decorators import login_required


app_name="biblioteca_app"

urlpatterns = [
    path('libros/ver', views.verlibros.as_view(), name='ver_libros'),
    path('mostrarlibro/<lb>/<v>', views.mostrarlibro.as_view(), name='mostrar_libro'),
    path('autores/<un>', views.ListaAutores.as_view(), name="lista_autores"),
    path('categorias/<un>', views.ListaCategorias.as_view(), name="lista_categorias"),
    path('editoriales/<un>', views.ListaEditoriales.as_view(), name="lista_editoriales"),
    path('revistas/<un>', views.ListaRevistas.as_view(), name="lista_revistas"),
    path('sucursales/<un>', views.ListaSucursales.as_view(), name="lista_sucursales"),
    path('servicios/<un>', views.ListaServicios.as_view(), name="lista_servicios"),
    path('reportes-Revistas/<un>', views.listaReportesLibrosAutores.as_view(), name="lista_reportesA"),
    path('reportes-Libros/<un>', views.listaReportesLibrosCategorias.as_view(), name="lista_reportesC"),
    path('reportes-Autores/<un>', views.opcionesReportesAutores.as_view(), name="opciones_reportesAutores"),
    path('reportes-Sucursales/<un>', views.opcionesReportesSucursales.as_view(), name="opciones_reportesSucursales"),
    re_path('z',views.lista.as_view(), name="veamos"),
    path('categoria/add/<un>', views.addCategoria.as_view(),name="agregar_categoria"),
    path('reporte/libro-categoria/<pk>/',views.CantidadCategoria_libros.as_view(),name="CantidadLibros-categoria"),
    path('reporte/revista-categoria/<pk>/', views.CantidadCategoria_revistas.as_view(), name="CantidadLibros-categoria"),
    path('reporte/libro-autor/<pk>/',views.CantidadAutor_libros_pdf.as_view(), name="CantidadLibros-autor"),
    path('reporte/sucursal-libro/<pk>/',views.CantidadSucursal_libros.as_view(), name="CantidadLibros-sucursal"),
    path('reporte/autor-libro/<pk>/',views.reporteAutoresLibro.as_view(), name="ReporteAutor_libro"),
    path('reporte/autor-nacionalidad/<pk>/',views.CantidadAutor_nacionalidad_pdf.as_view(), name="ReporteAutor_nacionalidad"),
    path('editorial/add/<un>', views.addEditorial.as_view(), name="agregar_editorial"),
    path('revista/add/<un>', views.addRevista.as_view(), name="agregar_revista"),
    path('sucursal/add/<un>', views.addSucursal.as_view(), name="agregar_sucursal"),
    path('servicio/add/<un>',views.addServicio.as_view(),name="agregar_servicio"),
    path('registro/<ca>/<us>',views.addUsuarioAdmin.as_view(), name="registro"),
    path('codigo/<ca>/<us>', views.addCodigoAdmin.as_view(), name='codigoAdmin'),
    path('editar-autor/<pk>/<un>', views.editAutor.as_view(), name="editar_autor"),
    path('editar-categoria/<pk>/<un>', views.editCategoria.as_view(), name="editar_categoria"),
    path('editar-editorial/<pk>/<un>', views.editEditorial.as_view(), name="editar_editorial"),
    path('editar-revista/<pk>/<un>', views.editRevista.as_view(), name="editar_revista"),
    path('editar-sucursal/<pk>/<un>',views.editSucursal.as_view(), name="editar_sucursal"),
    path('editar-servicio/<pk>/<un>', views.editServicio.as_view(), name="editar_servicio"),
    path('eliminar-autor/<pk>/<un>', views.deleteAutor.as_view(), name="eliminar_autor"),
    path('eliminar-libro/<pk>/<un>', views.deleteLibro.as_view(), name="eliminar_libro"),
    path('eliminar-categoria/<pk>/<un>', views.deleteCategoria.as_view(), name="eliminar_categoria"),
    path('eliminar-editorial/<pk>/<un>', views.deleteEditorial.as_view(), name="eliminar_editorial"),
    path('eliminar-revista/<pk>/<un>', views.deleteRevista.as_view(), name="eliminar_revista"),
    path('eliminar-sucursal/<pk>/<un>', views.deleteSucursal.as_view(), name="eliminar_sucursal"),
    path('eliminar-servicio/<pk>/<un>', views.deleteServicio.as_view(), name="eliminar_servicio"),
    path('editar-libro/<pk>/<un>', views.editLibro.as_view(), name="editar_libro"),
    path('buscar-libro/<pk>/<un>', views.buscarLibro.as_view(), name="buscar_libro"),
    path('buscar-editorial/<pk>/<un>', views.buscarEditorial.as_view(), name="buscar_editorial"),
    path('buscar-autor/<pk>/<un>', views.buscarAutor.as_view(), name="buscar_autor"),
    path('buscar-categoria/<pk>/<un>', views.buscarCategoria.as_view(), name="buscar_categoria"),
    path('buscar-revista/<pk>/<un>', views.buscarRevista.as_view(), name="buscar_revista"),
    path('buscar-sucursal/<pk>/<un>', views.buscarSucursal.as_view(), name="buscar_sucursal"),
    path('buscar-servicio/<pk>/<un>', views.buscarServicio.as_view(), name="buscar_servicio"),
    path('reporte/libros/<pk>/<fk>', views.rangoflibros.as_view(), name="filtrar_libros"),
    path('reporte/revistas/<pk>/<fk>', views.rangofrevistas.as_view(), name="filtrar_libros"),
    path('libros/<un>', views.ListaLibros.as_view(), name="lista_libros"),
    path('autor/add/<un>', views.addAutor.as_view(), name="Agregar_autores"),
    path('libro/add/<un>', views.addLibro.as_view(), name="Agregar_libros"),
    re_path('js', views.script.as_view(), name="js"),

    path('admin/<ca>', views.registro.as_view(), name="sd"),

    path('<ca>/er', views.errorsesion.as_view(), name="errorsesion"),
    path('er2/<cs>/', views.errorsesion2.as_view(), name="er2"),
    path('inicioA/<un>', views.Inicio.as_view(), name="index"),

    path('inicio/', views.inicioLogin.as_view(), name='inicioLogin'),
    path('errorLogin', views.errorLogin.as_view(), name="errorLogin"),
    path('login/add', views.addLogin.as_view(), name="addLogin"),
    path('inicioS/<us>', views.sesionLogin.as_view(), name='sesionLogin'),
    path('descripcionLibro/<lb>/<us>', views.descripcionLibro.as_view(), name='descripcion_libro'),
    path('comentar',views.comentar.as_view(), name='comentar'),
    path('Logout/<us>', views.cerarSesionLogin.as_view(), name='Logout'),
    path('fav',views.fav.as_view(), name='Fav'),
    path('saldo/<us>', views.saldo.as_view(), name='saldo'),
    path('agregarSaldo', views.addSaldo.as_view(), name='addSaldo'),
    path('comprar', views.comprar.as_view(), name='comprar'),
    path('MiBiblioteca/<us>', views.BibliotecaCompras.as_view(), name='MiBiblioteca'),
    path('enviarEmail/<us>', views.EnviarEmail.as_view(), name='enviarEmail'),


]