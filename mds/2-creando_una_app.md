# Creando una aplicación

Para crear una aplicación, primero se usa lo siguiente:

```Python
python3 manage.py startapp mi_app
```

Lo cual crea la carpeta _mi_app_. Hasta este momento, django no sabe qué hacer con esta app y actúa como si no existiera. Por lo tanto se tiene que conectar.

Se procede a editar la configuración de la app, para que pueda responder las peticiones:

Se crea el archivo **urls.py** y se edita la url que responderá la aplicación:
```Python
#mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    #ningun sub folder/de la clase views el método index/con nombre index
]
```

Se edita la vista que manda a llamar el método 
```Python
#mi_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Esta es mi mostriprueba")
```

Django al obtener una petición para un sitio, primero busca dentro de su archivo *urls.py*. Por tanto se procede a editarlo:

```Python
#mi_proyecto/urls.py
urlpatterns = [
    path('admin/', admin.site.urls), #Esto ya existía
    path('mi_app/', include('mi_app.urls')),
    #Esta línea es nueva, para que sepa cómo responder a las peticiones a misitio:8000/mi_app/
]
```

La razón por la cual se hace esto, es para que se pueda editar directamente el archivo de _urls.py_ dentro de _mi_app_ y no tengamos muchas urls dentro del proyecto principal.

Para probar que funcione correctamente, se necesita revisar en el navegador http://miservidor-django:8000/mi_app/

![Pantalla de Django](https://github.com/StrayChild01/pruebas-django/blob/master/imgs/mi_app-mostriprueba.png "Prueba django")

Nótese que después de hacer esto, la página de prueba dejará de funcionar, puesto que django ya tiene al menos una petición que responder.
