from django.urls import path
from . import views

app_name = "mi_app"
urlpatterns = [
    # ex: /mi_app/
    path('', views.index, name='index'),
    path('<int:depto_id>/', views.detalle_depto, name='detalle_depto'),
    path('<int:depto_id>/detalle_depto/', views.detalle_depto, name='detalle_depto'),
    path('<int:emp_id>/detalle_empleado/', views.detalle_empleado, name='detalle_empleado'),
    path('<int:dept_id>/lista_deptos/', views.lista_deptos, name='lista_deptos'),
    path('<int:emp_id>/lista_empleados/', views.lista_empleados, name='lista_empleados'),
]

