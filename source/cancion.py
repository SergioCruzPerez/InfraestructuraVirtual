#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import socket
import db

#Funciones para el microservicio DJ


    #Indica si la mezcla sonaría bien, comparando bpms.
def compararBPMS(nombrecancion,nombredeotra):
  bpms = db.devuelve_bpms(nombrecancion)
  bpmsotra = db.devuelve_bpms(nombredeotra)

  #Suena bien si ambas canciones se mueven entre un rango de 10bpms
  if abs( float(bpms) - float(bpmsotra) ) < 10.0 :
     return True
  else:
     return False
	
    #Indica si la mezcla sonaría bien comparando clane número-letra
def compararKey(nombrecancion,nombredeotra):
	claveN = db.devuelve_numero(nombrecancion)
	otrakeyN = db.devuelve_numero(nombredeotra)
	claveL = db.devuelve_letra(nombrecancion)
	otrakeyL = db.devuelve_letra(nombredeotra)  


 	#Para que suene bien..
	if abs( claveN - otrakeyN ) <= 2:
		uno = claveL
		dos = otrakeyL
		if   uno  -   dos <=1 or dos - uno <=1  :
			return True
		else:
			return False
	else:
		return False

    #Detectar si tengo conexion a Internet
def HayInternet():
         testConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         try:
                testConn.connect(('http://google.es', 80))
                testConn.close()
                return True
         except:
                testConn.close()
                return False

    #Función que guardará de lo que dispongo en la BBDD por si en algún momento me encuentro sin Internet
def Copia():
	canciones = ""
	if HayInternet():
		canciones = db.mostrar_canciones()
	
	return canciones
		
