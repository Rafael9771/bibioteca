from django.urls import path, re_path, include
from django.conf.urls import url, include

from . import views
from django.contrib.auth.views import LoginView ,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
from django.contrib.auth.decorators import login_required


app_name="biblioteca_app"

urlpatterns = [
    path('autores/<un>', views.ListaAutores.as_view(), name="lista_autores"),
    path('categorias/<un>', views.ListaCategorias.as_view(), name="lista_categorias"),
    path('editoriales/<un>', views.ListaEditoriales.as_view(), name="lista_editoriales"),
    path('revistas/<un>', views.ListaRevistas.as_view(), name="lista_revistas"),
    path('sucursales/<un>', views.ListaSucursales.as_view(), name="lista_sucursales"),
    path('servicios/<un>', views.ListaServicios.as_view(), name="lista_servicios"),
    re_path('reportesA', views.listaReportesLibrosAutores.as_view(), name="lista_reportesA"),
    re_path('reportesC', views.listaReportesLibrosCategorias.as_view(), name="lista_reportesC"),
    re_path('reportes-Autores', views.opcionesReportesAutores.as_view(), name="opciones_reportesAutores"),
    re_path('z',views.lista.as_view(), name="veamos"),
    path('categoria/add', views.addCategoria.as_view(),name="agregar_categoria"),
    path('reporte/libro-categoria/<pk>/',views.CantidadCategoria_libros.as_view(),name="CantidadLibros-categoria"),
    path('reporte/libro-autor/<pk>/',views.CantidadAutor_libros_pdf.as_view(), name="CantidadLibros-autor"),
    path('reporte/autor-libro/<pk>/',views.reporteAutoresLibro.as_view(), name="ReporteAutor_libro"),
    path('reporte/autor-nacionalidad/<pk>/',views.CantidadAutor_nacionalidad_pdf.as_view(), name="ReporteAutor_nacionalidad"),
    path('editorial/add', views.addEditorial.as_view(), name="agregar_editorial"),
    path('revista/add', views.addRevista.as_view(), name="agregar_revista"),
    path('sucursal/add', views.addSucursal.as_view(), name="agregar_sucursal"),
    path('servicio/add',views.addServicio.as_view(),name="agregar_servicio"),
    path('registro',views.addUsuario.as_view(), name="registro"),
    path('editar-autor/<pk>/', views.editAutor.as_view(), name="editar_autor"),
    path('editar-categoria/<pk>/', views.editCategoria.as_view(), name="editar_categoria"),
    path('editar-editorial/<pk>/', views.editEditorial.as_view(), name="editar_editorial"),
    path('editar-revista/<pk>/', views.editRevista.as_view(), name="editar_revista"),
    path('editar-sucursal/<pk>/',views.editSucursal.as_view(), name="editar_sucursal"),
    path('editar-servicio/<pk>/', views.editServicio.as_view(), name="editar_servicio"),
    path('eliminar-autor/<pk>/', views.deleteAutor.as_view(), name="eliminar_autor"),
    path('eliminar-libro/<pk>/', views.deleteLibro.as_view(), name="eliminar_libro"),
    path('eliminar-categoria/<pk>/', views.deleteCategoria.as_view(), name="eliminar_categoria"),
    path('eliminar-editorial/<pk>/', views.deleteEditorial.as_view(), name="eliminar_editorial"),
    path('eliminar-revista/<pk>/', views.deleteRevista.as_view(), name="eliminar_revista"),
    path('eliminar-sucursal/<pk>/', views.deleteSucursal.as_view(), name="eliminar_sucursal"),
    path('eliminar-servicio/<pk>/', views.deleteServicio.as_view(), name="eliminar_servicio"),
    path('editar-libro/<pk>/', views.editLibro.as_view(), name="editar_libro"),
    path('buscar-libro/<pk>/', views.buscarLibro.as_view(), name="buscar_libro"),
    path('buscar-editorial/<pk>/', views.buscarEditorial.as_view(), name="buscar_editorial"),
    path('buscar-autor/<pk>/', views.buscarAutor.as_view(), name="buscar_autor"),
    path('buscar-categoria/<pk>/', views.buscarCategoria.as_view(), name="buscar_categoria"),
    path('buscar-revista/<pk>/', views.buscarRevista.as_view(), name="buscar_revista"),
    path('buscar-sucursal/<pk>/', views.buscarSucursal.as_view(), name="buscar_sucursal"),
    path('buscar-servicio/<pk>/', views.buscarServicio.as_view(), name="buscar_servicio"),
    path('reporte/libros/<pk>/<fk>', views.rangoflibros.as_view(), name="filtrar_libros"),
    path('libros/<un>', views.ListaLibros.as_view(), name="lista_libros"),
    re_path('autor/add', views.addAutor.as_view(), name="Agregar_autores"),
    re_path('libro/add', views.addLibro.as_view(), name="Agregar_libros"),
    re_path('js', views.script.as_view(), name="js"),
    path('', views.registro.as_view(), name="sd"),
    path('er', views.errorsesion.as_view(), name="errorsesion"),
    path('er2/<cs>/', views.errorsesion2.as_view(), name="er2"),
    re_path('inicio', views.Inicio.as_view(), name="index"),


]