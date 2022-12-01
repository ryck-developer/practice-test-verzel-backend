from django.contrib import admin
from vehicle.models import *

@admin.register(VehicleModel)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'modelo', 'image', 'cor', 'preco', 'disponivel']

@admin.register(FabricanteModel)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(ModeloModel)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'marca']
