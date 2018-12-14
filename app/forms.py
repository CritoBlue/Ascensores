from django import forms 
from .models import Cliente, OrdenDeTrabajo, Ciudad, Comuna

class ClienteForm(forms.ModelForm):
    class Meta:
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

    
class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenDeTrabajo
        fields = (
            "idOT",
            "idCliente",
            "horaInicio",
            "horaTermino",
            "marcaAscensor",
            "modeloAscensor",
            "piezasCambiadas",
            )
            