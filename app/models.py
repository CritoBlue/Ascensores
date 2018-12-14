from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=30)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre	

class MarcaAscensor(models.Model):
	marca = models.CharField(max_length=30)
	def __str__(self):
		return self.marca

class ModeloAscensor(models.Model):
	modelo = models.CharField(max_length=30)
	marca = models.ForeignKey(MarcaAscensor, on_delete=models.CASCADE)
	def __str__(self):
		return self.modelo

class Cliente(models.Model):
	rut = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=80)
	ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
	comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
	telefono = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	tecnico = models.ManyToManyField(CustomUser)
	def __str__(self):
		return self.nombre

class OrdenDeTrabajo(models.Model):
	idOT = models.CharField(max_length=30, primary_key=True)
	idCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	fecha = models.DateField(default=timezone.now)
	horaInicio = models.CharField(max_length=5)
	horaTermino = models.CharField(max_length=5)
	marcaAscensor = models.ForeignKey(MarcaAscensor, on_delete=models.SET_NULL, null=True)
	modeloAscensor = models.ForeignKey(ModeloAscensor, on_delete=models.SET_NULL, null=True)
	piezasCambiadas = models.CharField(max_length=3)
	tecnico = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
	def publish(self):
		self.fecha = timezone.now()
		self.save()

	def __str__(self):
		return self.idOT