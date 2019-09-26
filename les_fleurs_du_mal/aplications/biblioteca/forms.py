from django import  forms

from .models import Libro


class editarLibro(forms.ModelForm):

    class Meta:
        model = Libro

        fields = [
            'titulo',
            'no_paginas',
            'fecha_creacion',
            'fecha_modificacion',
            'autor',
            'status',
        ]
        labels = {
            'titulo':'Titulo',
            'no_paginas':'Numero de Paginas',
            'fecha_modificacion':'Fecha de modificacion',
            'autor':'Autor',
        }
        widgets = {
            'titulo': forms.TextInput(),
            'no_paginas': forms.NumberInput(),
            'fecha_modificacion': forms.TextInput(),
            'autor': forms.TextInput(),
            'status':forms.TextInput(),
        }