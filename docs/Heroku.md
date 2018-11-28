# Heroku

## Instalación: (Windows)
Hay que tener previamente instalado git.

-Instalación de cliente de Heroku.

![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Descarga.png)

- Creación del proyecto, indicando nombre de éste y región.

![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Nombre.png)

- Realizamos la sincronicación automática con git.

![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Git.png)

- Realizado todo esto debemos pulsar el botón "DeployBranch" y si todo se ha realizado sin ningún fallo aparecerá el mensaje *Your app was successfully deployed.*

![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Despliegue.png)
Una vez desplegada la aplicación pulsando en el enlace de ésta podremos ver su funcionamiento.

Podemos también comprobar que esta corriendo al menos una instancia con el comandoo *heroku ps:scale web=1 -a (nombre de la aplicación)*

Si no nos acordamos del enlace de nuestra aplicación podremos ejecutar la orden *heroku open -a (nombre de la aplicación)*

## Destacar otras funcionalidades de heroku
Éstas pueden ser por ejemplo:
- *Ver aplicaciones activas* : heroku apps
- *Consultar el log para ver que ha podido fallar cuando se produce un fallo* : heroku logs --tail

## Procfile
Especifica los comandos que son ejecutados por los términos de la aplicación . Puede usar un Procfile para declarar una variedad de tipos de proceso , incluyendo:

- Servidor web de su aplicación
- Múltiples tipos de procesos de trabajo.
- Un proceso de singleton, como un reloj.
- Tareas para ejecutar antes de que se despliegue una nueva versión

### Procfile nombre y ubicación
El archivo Proc es siempre un archivo de texto simple que se nombra Procfile sin una extensión de archivo . Por ejemplo, Procfile.txt es válido.

El Procfile debe residir en el directorio raíz de su aplicación. No funciona si se coloca en otro lugar.

### Formato de archivo
Un Procfile declara sus tipos de proceso en líneas individuales, cada una con el siguiente formato: **<process type>: <command>**
- <process type> es un nombre alfanumérico para su comando, como web, worker, urgentworker, clock, y así sucesivamente.
- <command> indica el comando que cada proceso debe ejecutar al inicio.

### Problema
Para poner solución al problema de que Flask solamente procesan una solicitud a la vez, hacemos uso de Gunicorn, para servir nuestra app con más de un worker para que su rendimiento sea mayor.

- web: gunicorn <nombre_del_archivo_python sin extension>:app --log-file -
