import datetime, pytz
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils.timezone import utc
from .models import Departamento, Empleado
from django.urls import reverse

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

def edita_depto(request, dept_id):
    departamento = get_object_or_404(Departamento, pk=dept_id)
    return render(request, 'mi_app/edita_depto.html', {'departamento': departamento})

def set_depto(request, dept_id):
    departamento = get_object_or_404(Departamento, pk=dept_id)
    try:
        tz = pytz.timezone('America/Mexico_City')
    except (KeyError, Departamento.DoesNotExist):
        return render(request, 'mi_app:edita_depto', {
            'departamento': departamento,
            'mensaje_error': "No has seleccionado un departamento.",
        })
    else:
        now = datetime.datetime.utcnow().replace(tzinfo=tz)
        departamento.nombre_departamento = request.POST['nombre_departamento']
        departamento.nombre_gerente = request.POST['nombre_gerente']
        departamento.creado_depto = str(now)
        departamento.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mi_app:edita_depto', args=[departamento.pk]))

def edita_empleado(request, emp_id):
    response = "Estás viendo el listado de los empleados %s."
    return HttpResponse(response % emp_id)

