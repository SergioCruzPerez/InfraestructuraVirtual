# Almacen musical DJ
[![Build Status](https://travis-ci.org/SergioCruzPerez/InfraestructuraVirtual.svg?branch=master)](https://travis-ci.org/SergioCruzPerez/InfraestructuraVirtual)


Se plantea la creación de un almacén para canciones mediante el uso de un servidor en la nube. Estas canciones serán clasificadas dependiendo del género al que pertenezcan, bpms y claves. Este proyecto se ha desarrollado con la idea de hacer más sencilla la labor del DJ, funcionando como un dispositivo pendrive, además de proporcionar la posibilidad de compartir la música mezclada o producida con otros miembros de la comunidad, a la vez que uno pueda enriquecerse con todo tipo de música que se encuentre en la aplicación.

El porqué del desarrollo de esta aplicación se debe a que soy DJ y siempre he pensado que se debería de disponer de una aplicación que sustituya a un pendrive, puesto que estos dispositivos son pequeños y fáciles de extraviarse. También se fomentará el progreso de la carrera de un DJ y como peculiaridad destacar que funcionará también sin conexión a Internet, almacenando las canciones de las que disponía en la última conexión a Internet.

### Herramientas a usar

Todo es provisional a día de hoy puesto que se va a continuar investigando sobre que herramientas emplear y en el caso de que se encuentre algo más idóneo a lo elegido, se procederá a realizar un cambio.

* Lenguaje de programación empleado: Python.
* Se empleará MYSQL para almacenar todo tipo de información necesaria.
* Se usará JSON ya que es un lenguaje ideal para el intercambio de datos, además de ser totalmente independiente del lenguaje de programación.
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

Los métodos realizados en este hito comprueban si dos canciones sonarían bien a la hora de mezclarse, comprobar si hay conexión a Internet para uso futuro y lectura de campos de JSON.

### Por qué he elegido cada cosa
[Visita](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/explicacion.md)
