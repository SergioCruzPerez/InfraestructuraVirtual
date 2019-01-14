# Desplegando en Digital Ocean

## Empezando

Pero antes de empezar tenemos que tener instalado [Vagrant](https://www.vagrantup.com/downloads.html) el cual podríamos instalarlo desde terminal o desde la página web.

Se debe de bajar desde la página web puesto que si no tendremos problemas de diversos tipos como podrían ser errores en la verificación de los certificados SSL.

Posteriormente debemos de tener instalado el **plugin** que proporciona Vagrant para Digital Ocean de la siguiente forma:

~~~
$vagrant plugin install vagrant-digitalocean
~~~

Instalado el plugin procedemos a crear nuestro vagrantfile donde indicaremos toda la configuración que deseamos que satisfaga nuestra máquina.


## Creación de un Vagrantfile

El [Vagrantfile](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/Vagrantfile) es un archivo de Ruby utilizado para configurar Vagrant por proyecto. La función principal de [Vagrantfile](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/Vagrantfile) es describir las máquinas virtuales necesarias para un proyecto, así como la forma de configurar y aprovisionar estas máquinas.

La idea es que cuando un desarrollador sincroniza su fichero vagrantfile, simplemente con lanzar el comando vagrant up obtiene un entorno virtual totalmente aprovisionado para desarrollar ese producto.

Debemos de crearlo en la raíz del proyecto y nos encontramos los siguientes parámetros, por ejemplo:

En mi [Vagrantfile](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/Vagrantfile) encontraremos detalladamente las opciones para construir mi máquina y el porqué de la elección.

## Problema con su correspondiente solución

He comentado en mi vagrantfile las órdenes correspondientes a la ejecución de Ansible para que realizara el provisionamiento puesto que obteníamos el siguiente error.
![img]()
Para solventar esto he tenido que añadir en el fichero /etc/ansible/hosts lo siguiente:

![img]() y esto debe de realizarse tras ejecutar la orden **vagrant up --provider=digital_ocean puesto que es cuando se nos asigna una ip(en ipv4) a nuestra máquina.
![img]()

Una vez realizado esto el provisionamiento se lleva a cabo sin ningún tipo de problema

![img]()

## Aprovisionamiento

Ansible es una herramienta open-source desarrollada en python y comercialmente ofrecida por AnsibleWorks que la definen como un motor de orquestación muy simple que automatiza las tareas necesarias que deseamos realizar sobre un host, se apoya en un fichero llamado [playbook.yml](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/provision/playbook.yml) donde con become indicamos que las tareas se ejecuten en modo superusuario, y dentro del directorio *Tasks* definimos las tareas que se deben ejecutar en el host, donde con **name** indicamos el nombre de la tarea y con **command** el comando a ejecutar, destacando que en la tarea de clonar mi repositorio de Github, empleamos git en vez de command con una serie de parámetros que son especificados en mi fichero [playbook.yml](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/provision/playbook.yml)

- Debemos de tener instalado en nuestro host [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-the-control-machine)

- Debemos de tener una versión reciente de OpenSSH que admita ControlPersist, nada de usar LibreSSL puesto que todo serán inconvenientes relacionados con la comunicación y visibilidad entre máquinas a la hora de realizar el aprovisionamiento.

Una vez realizado esto, ejecutando la orden **vagrant up** desplegaríamos nuestra máquina y estaría lista para ser usada.

## Usando Fabric

Fabric es una biblioteca de alto nivel de Python (2.7, 3.4+) diseñada para ejecutar comandos de shell de forma remota a través de SSH, y ofrece a cambio objetos útiles de Python todo esto a traves de un fichero llamado [fabfile.py](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/despliegue/fabfile.py)

Ejecutaremos cualquier función del fichero fabfile.py de la siguiente forma:

~~~
fab -f despliegue/fabfile.py -H vagrant@51.144.180.183 (Tarea a realizar)
~~~

Ejemplos de uso:

- Ejecución de tarea Start
![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Start.png)

- Ejecución de tarea Stop
![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Stop.png)

- Ejecución de tarea Install
![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Install.png)

- Ejecución de tarea Delete
![img](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/docs/imagenes/Delete.png)
