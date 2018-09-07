# Primeros pasos

Para crear un proyecto, primero se usa lo siguiente:

```Python
django-admin startproject mi_proyecto
```

Lo cual crea la carpeta _mi_proyecto_, dentro de esta, se modifica el archivo **~/mi_proyecto/settings.py**

Se cambia de esto:
```Shell
ALLOWED_HOSTS = []
```

A esto:

```Shell
ALLOWED_HOSTS = ['*']
```

Para permitir que se pueda acceder desde cualquier ip.

Si se quiere habilitar la bitácora para saber qué está pasando, se agrega lo siguiente al final del archivo:

```Javascript
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
        'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format':
                '%(levelname)s %(message)s'
        },
    },
}
```
Para probar que funcione, se ejecuta lo siguiente:

```Shell
python3 manage.py runserver 0:8000
```

Para comprobar que django esté corriendo, en el navegador se va a http://servidor-django:8000 y deberá mostrar lo siguiente:

![Pantalla de Django](https://github.com/StrayChild01/pruebas-django/blob/master/imgs/django-test.png "Prueba django")

