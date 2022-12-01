from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from vehicle.serializers import *

# ALTERAR PARA TRUE QUANDO FOR PARA PRODUÇÃO 
# OU PERMITIR SOMENTE LEITURA NOS TESTES
PRODUCTION_ = True

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all().order_by('preco')
    serializer_class = VehicleSerializer
    if PRODUCTION_:
        #READ-ONLY PERMISSION
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        # CRUD TEST API ALLOWED FOR ALL
        permission_classes = [permissions.AllowAny]

class FabricanteViewSet(viewsets.ModelViewSet):
    queryset = FabricanteModel.objects.all()
    serializer_class = FabricanteSerializer
    if PRODUCTION_:
        #READ-ONLY PERMISSION
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        # CRUD TEST API ALLOWED FOR ALL
        permission_classes = [permissions.AllowAny]

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = ModeloModel.objects.all()
    serializer_class = ModeloSerializer
    if PRODUCTION_:
        #READ-ONLY PERMISSION
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        # CRUD TEST API ALLOWED FOR ALL
        permission_classes = [permissions.AllowAny]


