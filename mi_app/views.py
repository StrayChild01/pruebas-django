from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Departamento, Empleado


# Create your views here.
def index(request):
    todos_departamentos = Departamento.objects.all()
    template = loader.get_template('mi_app/index.html')
    #salida = ', '.join([d.nombre_departamento for d in todos_departamentos])
    #return HttpResponse(salida)
    context = {
        'todos_departamentos': todos_departamentos,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'mi_app/index.html', context)

def detalle_depto(request, depto_id):
    #try:
    #    departamento = Departamento.objects.get(pk=depto_id)
    #except Departamento.DoesNotExist:
    #    raise Http404("Lo sentimos, este departamento no existe")
    departamento = get_object_or_404(Departamento, pk=depto_id)
        
    return render(request, 'mi_app/detalle_depto.html', {'departamento': departamento})

def detalle_empleado(request, emp_id):
    try:
        empleado = Empleado.objects.get(pk=emp_id)
    except Empleado.DoesNotExist:
        raise Http404("Lo sentimos, este empleado no existe")

    return render(request, 'mi_app/detalle_emp.html', {'empleado': empleado})

def lista_deptos(request, dept_id):
    response = "Estás viendo el listado de los departamentos %s."
    return HttpResponse(response % dept_id)
    
def lista_empleados(request, emp_id):
    response = "Estás viendo el listado de los empleados %s."
    return HttpResponse(response % emp_id)

