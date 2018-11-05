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
