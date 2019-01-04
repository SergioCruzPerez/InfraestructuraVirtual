# Vagrant Azure Provider

Esto es un complemento de Vagrant que agrega el proveedor de Microsoft Azure a Vagrant, lo que le permite a Vagrant controlar y aprovisionar máquinas en Microsoft Azure.

## Empezando

Pero antes de empezar tenemos que tener instalado [Vagrant](https://www.vagrantup.com/downloads.html) el cual podríamos instalarlo desde terminal o desde la página web.

Se debe de bajar desde la página web puesto que si no tendremos problemas de diversos tipos como podrían ser errores en la verificación de los certificados SSL.

Posteriormente debemos de tener instalado el **plugin** que proporciona Vagrant para Azure de la siguiente forma:

~~~
$ vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
$ vagrant plugin instalar vagrant-azure
$ vagrant up --provider = azure
~~~

## Azure Active Directory (AAD)

Debemos de seguir los siguientes pasos:

1. [Instale el CLI de Azure](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)

2. **az login** para iniciar sesión en azure.

3. Ejecute **az ad sp create-for-rbac** para crear una aplicación de Azure Active Directory con acceso a Azure Resource Manager para la suscripción actual de Azure. Si desea ejecutar esto para una suscripción de Azure distinta emplee **az account set --subscription 'your subscription name'**

4. Una vez realizado esto ejecutaremos **az ad sp create-for-rbac** y **az account list --query "[?isDefault].id" -o tsv**.

Con el primer comando obtendremos una salida como esta:

~~~
{
  "appId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  "displayName": "some-display-name",
  "name": "http://azure-cli-2017-04-03-15-30-52",
  "password": "XXXXXXXXXXXXXXXXXXXX",
  "tenant": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
}
~~~

Los valores tenant, appId y password se corresponden con los valores de configuración azure.tenant_id, azure.client_id y azure.client_secret en nuestro Vagrantfile.

Y con el segundo comando obtendremos el id de nuestra subscripción que se corresponde con el valor azure.subscription_id.

## Creación de un Vagrantfile

El [Vagrantfile](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/Vagrantfile) es un archivo de Ruby utilizado para configurar Vagrant por proyecto. La función principal de [Vagrantfile](https://github.com/SergioCruzPerez/InfraestructuraVirtual/blob/master/Vagrantfile) es describir las máquinas virtuales necesarias para un proyecto, así como la forma de configurar y aprovisionar estas máquinas.

La idea es que cuando un desarrollador sincroniza su fichero vagrantfile, simplemente con lanzar el comando vagrant up obtiene un entorno virtual totalmente aprovisionado para desarrollar ese producto.

Debemos de crearlo en la raíz del proyecto y nos encontramos los siguientes parámetros, por ejemplo:

- tenant_id: Tu Azure Active Directory Tenant Id.
- client_id: Tu Azure Active Directory application client id.
- client_secret: Tu Azure Active Directory application client secret.
- subscription_id: La subscripcion de Azure que queremos usar.
- vm_name: Nombre de la máquina virtual
- vm_size: Tamaño de máquina virtual que se utilizará: el valor predeterminado es 'Standard_DS2_v2'.
- m_image_urn: Nombre de la máquina virtual que se usará: por defecto es 'canonical: ubuntuserver: 16.04-LTS: latest'.
- tcp_endpoints: nos permite abrir puertos de entrada al servicio y poder acceder al servicio web.
- Con config.vm.provision indicamos el aprovisionador a usar, en nuestro caso ansible y posteriormente indicamos donde se encuentra el fichero de aprovisionamiento.

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
