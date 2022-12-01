from django.db import models
import uuid

class VehicleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=130)
    modelo = models.ForeignKey('ModeloModel', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media')
    cor = models.CharField(max_length=30)
    preco = models.FloatField()
    disponivel = models.BooleanField(default=True)

    def __str__ (self):
        return self.nome

class FabricanteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.nome

class ModeloModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey('FabricanteModel', on_delete=models.PROTECT)

    def __str__ (self):
        return self.nome