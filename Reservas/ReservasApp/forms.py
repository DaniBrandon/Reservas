from django import forms

class HabitacionForm(forms.Form) :
    descripcion = forms.CharField(label='Descripción', max_length=60)