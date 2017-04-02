# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision "shell", path: "pg_config.sh"
  # config.vm.box = "hashicorp/precise32"
  config.vm.box = "ubuntu/trusty32"
  config.vm.network "forwarded_port", guest: 1000, host: 1000
  config.vm.network "forwarded_port", guest: 2000, host: 2000
  config.vm.network "forwarded_port", guest: 3000, host: 3000
end
