from django.shortcuts import render, redirect
from .forms import ClienteForm, OrdenTrabajoForm
from .models import OrdenDeTrabajo
from django.views.generic import TemplateView
from rest_framework import viewsets
from app.serializers import OTSerializer

# Create your views here.

#class IndexView(TemplateView):
#    template_name = 'app/index.html'

def base(request):
	return render(request, 'app/base.html')

def index(request):
	results = OrdenDeTrabajo.objects.all()
	context = {
		'results' : results,
	}
	return render(request, 'app/index.html', context)

def cliente(request):
	if request.method == "POST":
		form = ClienteForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			form.save_m2m()
			instance.tecnico.add(request.user)
			return redirect('/')
	else:
		form = ClienteForm()
	return render(request, 'app/cliente.html', {'form':form})

def orden(request):
	if request.method == "POST":
		form = OrdenTrabajoForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.tecnico = request.user
			instance.save()
			return redirect('/')
	else:
		form = OrdenTrabajoForm()
	return render(request, 'app/orden.html', {'form':form})

class OTViewSet (viewsets.ModelViewSet):
	queryset = OrdenDeTrabajo.objects.all().order_by('fecha')
	serializer_class = OTSerializer

def getdata(request):
	results=OrdenDeTrabajo.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)
