# Docker

Podremos encontrar todo lo relativo a Docker en : https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Pasos de instalación:
Se recomienda desinstalar, por si se tuviera una versión antigua: **sudo apt-get remove docker docker-engine docker.io**
(img)

Antes de instalar Docker en una nueva máquina debemos configurar el repositorio donde va a estar Docker.
Después instalaremos y actualizaremos Docker desde el repositorio.

### Configuración del repo
**sudo apt-get update**

Instalamos paquetes esenciales para poder trabajar con Docker

**sudo apt-get install apt-transport-https
sudo apt-get install ca-certificates
sudo apt-get install curl
sudo apt-get install software-properties-common**

Añadimos la key GPG oficial de docker con curl

**curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -**

Verificamos la clave utilizando
**sudo apt-key fingerprint**

Configuramos el repositorio en modo estable

**sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"**


#### Instalación de docker ce

1. Instalamos la última versión:

**sudo apt-get update
sudo apt-get install docker-ce**

2. Verificar la instalación:

**sudo docker run hello-world**

Si todo ha ido correctamente deberá aparecer lo que se muestra en la imagen

![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/dockerhello.png)

Con *systemctl status docker.service* podríamos ver si el servicio de docker está activo o no.


Completada la instalación procedemos a:

###  DEPENDENCIAS PARA MI APLICACIÓN

Crear un **Docker file** (Python):
Documentación: https://docs.docker.com/samples/library/python/#run-a-single-python-script

Aquí tienes  el enlace a mi [dockerfile](https://github.com/joseviro/ProyectoTPV/blob/master/Dockerfile).

## Para construir y probar que todo funciona correctamente en local basta con:

**sudo docker build -t iv . Con lo que construimos la imagen
sudo docker run --rm -p 80:80 -it iv**


-p indicamos el puerto.
-t asigna un nuevo terminal dentro del contenedor.
-i nos permite hacer una conexión interactiva
–rm elimina automáticamente el contenedor cuando el proceso finaliza.

## Docker hub
Documentación:
https://docs.docker.com/docker-hub/builds/#understand-the-build-process

Creamos una cuenta de docker hub, sincronizándola con github para que todo cambio que se efectúe en github también se haga en docker.

![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/dockerhub.png)


![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/linkdockergithub.png)

Tenemos que clickar en create -> create automated build y tras indicar a que proyecto queremos vincular el docker y una pequeña descripción, estará todo listo

**Podríamos ver que todo lo hecho hasta ahora funciona correctamente de la siguiente forma**
*Crearíamos la imagen correspondiente*
sudo docker build -t nombreusuario/nombrecontenedor(sería nombre de la imagen) .
*Una vez creada la imagen*
sudo docker run --rm -it nombredelaimagen

## Despliegue en heroku
Creamos una nueva aplicación: en mi caso contenedoriv y procedemos de la misma forma que se explicó en el hito 3.

Debemos de especificar que vamos a crear un contenedor con las órdenes propias de Container Register.

Download Heroku cli.
**heroku login --interactive**
Log in to Container Registry
**docker ps**
Now you can sign into Container Registry
**heroku container:login**
Push yout Docker-based app
**heroku container:push web -a nombrecontenedor**
Deploy the changes
**heroku container:release web**

## heroku.yml
Documentación: https://devcenter.heroku.com/articles/build-docker-images-heroku-yml

Este archivo es necesario para indicar como debe construirse el contenedor y como ejecutarse en caso de que no queramos que ejecute la orden **Run** del dockerfile

[Enlace a mi heroku.yml](https://github.com/joseviro/ProyectoTPV/blob/master/heroku.yml)


**heroku apps:info -a contenedoriv** nos confirmaría que lo que hemos subido es un contenedor y no una app.
~~~

![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/stackContainer.png)

![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/Stackheroku-18.png)
