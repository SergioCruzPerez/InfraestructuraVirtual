# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  #Configuración predeterminada, es decir para todos los proveedores iría aquí.
  # Usamos la opción que nos proporciona Vagrantfile para copiar en mi caso los archivos .mp3 
  config.vm.provision "file", source: "~/Desktop/InfraestructuraVirtual/static", destination: "static"
 
#Para dotar a mi droplet de nombre y quitar el que tiene por defecto,'default'
 config.vm.define "almacen-dj" do |config|
  config.vm.provider :digital_ocean do |digital_ocean, override|
#primer parámetro de config.vm.provider, nombre del proveedor a configurar y el segundo parámetro es necesario puesto que indica que la configuración que se va a realizar es solo para el proveedor indicado por el primer argumento.  
    # Indicamos la caja con la que se levantará la máquina. Debe de ser una caja exixtente en el catálogo de cajas de la página de Vagrant
    override.vm.box="digital_ocean"
    # override.vm.box_download_location_trusted = false 
    # Comentado porque por defecto es falso, es muy importante para que las credenciales si las especificamos se usen solo en la primera solicitud HTTP, si no es así nuestra máquina podría ser muy vulnerable.
    # Esta configuración es opcional, pero la proporciono por si la caja no existe en el sistema en el que se va a hacer vagrant up. Por defecto es nulo
    override.vm.box="https://github.com/devopsgroup-io/vagrant-digitalocean/raw/master/box/digital_ocean.box"
    # Segundos que Vagrant espera cuando se ejcuta vagrant halt. Me interesa que sea mas corto que 60 segundos.
    override.vm.graceful_halt_timeout = 40
    # Especifico la ruta en la que se almacena la clave privada SSH.
    override.ssh.private_key_path='~/.ssh/id_rsa'
    
    # Especificamos el Token personal de acceso de Digital Ocean.
    digital_ocean.token=ENV['TOKEN']
    # Especificamos la imagen a usar al crear un nuevo Droplet. Por defecto es Ubuntu14 pero voy a usar Ubuntu 16 que es en el SO en el que he desarrollado mi aplicación. Podemos listar las imágenes disponibles con vagrant digitalocean-list images $TOKEN
   digital_ocean.image="ubuntu-16-04-x64"
    # Especificamos la región para crear el nuevo droplet. Podemos listarlos con el comando vagrant digitalocean-list regions $TOKEN
   digital_ocean.region="lon1"
    # Especificamos tamaño al crear el nuevo droplet. Podemos listarlos con vagrant digitalocean-list sizes $TOKEN
   digital_ocean.size="1gb"
   end
 end
    
    #Ejecutar Ansible en mi máquina Vagrant.
   # config.vm.provision :ansible do |ansible|
    #  ansible.playbook="provision/playbook.yml"
    #end
    
end
