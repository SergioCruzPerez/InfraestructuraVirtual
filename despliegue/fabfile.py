from fabric.api import *
import os

def Update():
	""" Actualizar por si hubiera posibles cambios """
	
	with cd ('InfraestructuraVirtual'):
	  run('git pull && pip install -r requirements.txt')

def Install():
	""" Instalacion usando nuestro requirements.txt que contiene los requisitos necesarios """
	""" existe = os.direxists(os.path.join(os.getcwd()), 'home/vagrant/InfraestructuraVirtual'))
	print(existe)
	if existe:
         run('git pull && pip install -r requirements.txt') 
	else: """
        run('git clone https://github.com/SergioCruzPerez/InfraestructuraVirtual.git')
        run('sudo apt-get update && sudo apt-get install python-pip')
        run('cd InfraestructuraVirtual && sudo pip install -r requirements.txt')

def Stop():
	""" Parar la aplicacion matando el proceso que usa gunicorn 
	 
	run('sudo pkill gunicorn') No correcto porque no sabemos que procesos pueden estar ejecutandose en nuestra maquina con gunicorn y con este comando matariamos todos """
	run("sudo kill $(ps -ef | grep gunicorn | awk '{print $2}')")


def Delete():
	""" Eliminar mi aplicacion """
	run('sudo rm -rf ./InfraestructuraVirtual')

def Start():
	""" Iniciar mi aplicacion """
	
	Update()
	with cd ("InfraestructuraVirtual"):
	  run('sudo gunicorn APLICACION_WEB:app --log-file=- --bind 0.0.0.0:80')
	
