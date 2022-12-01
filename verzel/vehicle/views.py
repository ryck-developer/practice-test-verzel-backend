from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from vehicle.serializers import *


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all().order_by('preco')
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

class FabricanteViewSet(viewsets.ModelViewSet):
    queryset = FabricanteModel.objects.all()
    serializer_class = FabricanteSerializer
    permission_classes = [permissions.IsAuthenticated]

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = ModeloModel.objects.all()
    serializer_class = ModeloSerializer
    permission_classes = [permissions.IsAuthenticated]


