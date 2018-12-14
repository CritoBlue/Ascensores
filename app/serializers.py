from .models import Cliente, OrdenDeTrabajo
from rest_framework import serializers

class OTSerializer(serializers.HyperlinkedModelSerializer):
	class meta:
		model = OrdenDeTrabajo
		fields = ("idOT",
            "idCliente",
            "fecha",
            "horaInicio",
            "horaTermino",
            "marcaAscensor",
            "modeloAscensor",
            "piezasCambiadas",
            "tecnico",
            )

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	class meta:
		model = Cliente
		fields = (
            "rut",
            "nombre",
            "direccion",
            "ciudad",
            "comuna",
            "telefono",
            "email",
        )