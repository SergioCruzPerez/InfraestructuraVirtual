#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import socket

class canciones():
    """Clase para el microservicio DJ"""


    def __init__(self,n):
        try:
            if os.path.exists('data/unacancion.json'):
                with open('data/unacancion.json', 'r') as f:
                    info = json.load(f)
                    i = 0
                    while i < len(info['songs']): #Cancion que deseo cargar
                        if info['songs'][i]['nombre'] == n:
                            self.nombre = info['songs'][i]['nombre']
                            self.artista = info['songs'][i]['artista']
                            self.ruta = info['songs'][i]['ruta']
                            self.bpms = info['songs'][i]['bpms']
                            self.claveN = info['songs'][i]['claveN']
                            self.claveL = info['songs'][i]['claveL']
                            break
                        else:
                            i+=1

            else:
                raise IOError("No se encuentra 'unacancion.json'")

        except IOError as fallo:
             print("Error {} leyendo unacancion.json".format( fallo ) )


    #Indica si la mezcla sonaría bien, comparando bpms.
    def compararBPMS(self,otra):
         with open('data/unacancion.json') as f:
            otrainfo = json.load(f)
            i=0
            while i < len(otrainfo['songs']): #Cancion que deseo cargar
                if otrainfo['songs'][i]['nombre'] == otra:
                    otrabpms= otrainfo['songs'][i]['bpms']
                    break
                else:
                    i+=1

            #Suena bien si ambas canciones se mueven entre un rango de 10bpms
            if abs( self.bpms - otrabpms ) < 10 :
                return True
            else:
                return False

    def compararKey(self,otra):
          with open('data/unacancion.json') as f:
             otrainfo = json.load(f)
             i=0
             while i < len(otrainfo['songs']): #Cancion que deseo cargar
                 if otrainfo['songs'][i]['nombre'] == otra:
                     otrakeyN= otrainfo['songs'][i]['claveN']
                     otrakeyL= otrainfo['songs'][i]['claveL']
                     break
                 else:
                     i+=1


             #Para que suene bien..
             if abs( self.claveN - otrakeyN ) <= 2:
                uno = ord (self.claveL)
                dos = ord (otrakeyL)
                if   uno  -   dos <=1  :
                    return True
                else:
                    return False
             else:
                return False

            #Detectar si tengo conexion a Internet
    def HayInternet(self):
         testConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         try:
                testConn.connect(('http://google.es', 80))
                testConn.close()
                return True
         except:
                testConn.close()
                return False
