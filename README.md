# Almacen musical DJ
[![Build Status](https://travis-ci.org/SergioCruzPerez/InfraestructuraVirtual.svg?branch=master)](https://travis-ci.org/SergioCruzPerez/InfraestructuraVirtual)


Se plantea la creación de un almacén para canciones mediante el uso de un servidor en la nube. Estas canciones serán clasificadas dependiendo del género al que pertenezcan, bpms y claves. Este proyecto se ha desarrollado con la idea de hacer más sencilla la labor del DJ, funcionando como un dispositivo pendrive, además de proporcionar la posibilidad de compartir la música mezclada o producida con otros miembros de la comunidad, a la vez que uno pueda enriquecerse con todo tipo de música que se encuentre en la aplicación.

El porqué del desarrollo de esta aplicación se debe a que soy DJ y siempre he pensado que se debería de disponer de una aplicación que sustituya un pendrive, puesto que estos dispositivos son pequeños y fáciles de extraviarse. También fomentará el progreso de la carrera de DJ y como peculiaridad destacar que funcionará también sin conexión a Internet, almacenando canciones de las que disponía en la última conexión a Internet.

### Herramientas a usar

Todo es provisional a día de hoy puesto que se va a continuar investigando sobre que herramientas emplear y en el caso de que se encuentre algo más idóneo a lo elegido, se procederá a realizar un cambio.

* Lenguaje de programación empleado: Python.
* He empleado la funcionalidad de [Postgres SQL que ofrece Heroku](https://devcenter.heroku.com/articles/heroku-postgresql) gracias al uso de psycopg.
* Para poder probar el funcionamiento de las clases y métodos que componen nuestra aplicación usaremos Unittest.
* Framework a emplear será Flask.

### Instalación

pip install -r requirements.txt

### Ejecución de test

Al estar hechos con unittest bastaría con hacer:
python nombre_clase_test.py

### Ejecución

python cancion.py

### Uso

Los métodos realizados comprueban si dos canciones sonarían bien a la hora de mezclarse, comprobar si hay conexión a Internet para uso futuro y lectura de campos de JSON.

### Por qué he elegido cada cosa
[Visita](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/explicacion.md)

## PaaS Elegido: Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

He elegido Heroku porque es gratuito, intuitivo y he encontrado mucha documentación al respecto que sé que me ayudaría en problemas presentes y futuros que se me pudieran presentar. Destacar que la comunidad de Heroku es muy activa y esto se agradece.

**despliegue** : [AlmacénDJ](https://almacen-dj.herokuapp.com/)

Documentación [heroku](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/Heroku.md)

## Docker
En [Documentación](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/docker.md) se explican que realizar para poder poner en marcha un contenedor docker.

Contenedor: [https://contenedoriv.herokuapp.com/](https://contenedoriv.herokuapp.com/)

Repositorio en docker hub: https://hub.docker.com/r/sergiocruzperez/infraestructuravirtual/

## IaaS Vagrant
Despliegue final:51.144.180.183

[Consultar documentación de todo lo realizado](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/hito5.md)
