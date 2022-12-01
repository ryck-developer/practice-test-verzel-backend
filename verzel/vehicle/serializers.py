from rest_framework import serializers
from vehicle.models import *


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'

class FabricanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FabricanteModel
        fields = '__all__'

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModeloModel
        fields = '__all__'