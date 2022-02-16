from django.contrib import admin

# Register your models here.
from .models import TipoHabitacion
from .models import Habitacion

admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)