from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)
    nombre_gerente = models.CharField(max_length=100)
    creado_depto=models.DateTimeField('Creado Departamento')
    def __str__(self):
        return self.nombre_departamento + \
            " - " + \
            self.nombre_gerente + \
            " - " + \
            str(self.creado_depto)

class Empleado(models.Model):
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    def __str__(self):
        return str(self.departamento) + \
            " - " + \
            self.nombre + \
            " - " + \
            self.alias


