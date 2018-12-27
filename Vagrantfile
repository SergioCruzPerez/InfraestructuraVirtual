# Every Vagrant development environment requires a box. You # -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "azure"
  config.vm.box_url = "https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box"

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  config.vm.provider :azure do |azure, override|
    azure.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:16.04.201612210'
		azure.vm_size = 'Basic_A0'
		azure.location = 'westeurope'
		azure.vm_name = 'serviciodalmacenddjdefini'
		azure.tcp_endpoints = '80'

    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
  end

  # configuration of ansible
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provision/playbook.yml"
  end

end
