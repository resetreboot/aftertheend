# django imports
from django.contrib import admin

# project imports
from fichas.models import Ficha, Raza

# Register your models here.
admin.site.register(Ficha)
admin.site.register(Raza)
