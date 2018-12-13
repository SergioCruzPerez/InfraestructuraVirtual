#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psycopg2

DATABASE_URL = "postgres://wvatsirycufwhc:216a7248a597969d2e9afd4b6f6a7b63c529ab261c73f26c2cbb97bb002edfa2@ec2-54-217-237-93.eu-west-1.compute.amazonaws.com:5432/db6mssc729tmgi"

def insertar_cancion(nombre,artista,bpms,claveN,claveL):
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("INSERT INTO canciones(nombre,artista,bpms,claveN,claveL) VALUES (%s,%s,%s,%s,%s);", [nombre,artista,bpms,claveN,claveL] )
	conexion.commit()
	c.close()
	conexion.close()

def borrar_cancion(nombre):
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("DELETE FROM canciones WHERE nombre = %s",[nombre])
	conexion.commit()
	c.close()
	conexion.close()

def mostrar_canciones():
	""" Se añadirá en futuras versiones posibilidades de listado """
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("SELECT * FROM canciones ORDER BY nombre;")
	canciones = ""

	cancion = c.fetchall()

	for song in cancion:
		canciones += str(song[0]) + " " + str(song[1]) + " " + str(song[2]) + " " + str(song[3]) + " " + str(song[4]) + "\n"

	print(canciones)

	c.close()
	conexion.close()
	

def devuelve_bpms(cancion):
	bpm = None
	a_devolver = ""
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("SELECT bpms FROM canciones WHERE nombre=%s", [cancion])
	bpm = c.fetchone()
	a_devolver = str(bpm[0])

	c.close()
	conexion.close()
	
	return a_devolver

def devuelve_numero(cancion):
	n = None
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("SELECT claveN FROM canciones WHERE nombre=%s", [cancion])
	n = c.fetchone()
	a_devolver_numero = str(n[0])
	

	c.close()
	conexion.close()
	
	return int(a_devolver_numero)

def devuelve_letra(cancion):
	l = None
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("SELECT claveL FROM canciones WHERE nombre=%s", [cancion])
	l = c.fetchone()
	a_devolver_letra = str(l[0])

	c.close()
	conexion.close()
	
	return ord(a_devolver_letra)

def buscar_por_bpms(bpms):
	canciones = []
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("SELECT nombre FROM canciones WHERE bpms=%s ORDER BY nombre", [bpms])
	for cancion in c:
		canciones.append(cancion[0])

	c.close()
	conexion.close()
	
	return canciones

def buscar_por_nombre(nombre):
	cancion = None
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	c.execute("SELECT * FROM canciones WHERE nombre=%s", [nombre])
	cancion = c.fetchone()

	c.close()
	conexion.close()


	return cancion

def numero_canciones_almacenadas():
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	c = conexion.cursor()
	numero = None
	c.execute("SELECT nombre FROM canciones;")
	
	
	numero = len(c.fetchall())

	return numero


def buscar_adecuadas(nombre):
	conexion = psycopg2.connect(DATABASE_URL, sslmode='require')
	b = conexion.cursor()
	b.execute("SELECT bpms FROM canciones WHERE nombre=%s", [nombre])
	bpm = b.fetchone()

	b.close()

	c = conexion.cursor()
	c.execute("SELECT claveN FROM canciones WHERE nombre=%s", [nombre])

	claven = c.fetchone()

	c.close()

	definitivo = conexion.cursor()
	definitivo.execute("SELECT * FROM canciones WHERE ABS(bpms-%s) <= 5 AND ABS(claveN-%s) <= 2 ORDER BY nombre;", [bpm,claven])

	print("Posibilidades:",definitivo.rowcount)
	row = definitivo.fetchone()

	while row is not None:
		print(row)
		row = definitivo.fetchone()

	definitivo.close()
	conexion.close()
	

	


	

	
