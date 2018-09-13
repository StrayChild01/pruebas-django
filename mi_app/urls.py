from django.urls import path
from . import views

app_name = "mi_app"
urlpatterns = [
    # ex: /mi_app/
    path('', views.index, name='index'),
    path('<int:depto_id>/', views.detalle_depto, name='detalle_depto'),
    path('<int:depto_id>/detalle_depto/', views.detalle_depto, name='detalle_depto'),
    path('<int:emp_id>/detalle_empleado/', views.detalle_empleado, name='detalle_empleado'),
    path('<int:dept_id>/edita_depto/', views.edita_depto, name='edita_depto'),
    path('<int:dept_id>/set_depto/', views.set_depto, name='set_depto'),
    path('<int:emp_id>/edita_empleado/', views.edita_empleado, name='edita_empleado'),
]