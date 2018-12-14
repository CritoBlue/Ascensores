from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(MarcaAscensor)
admin.site.register(ModeloAscensor)
admin.site.register(OrdenDeTrabajo)