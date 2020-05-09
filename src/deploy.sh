apt-get update
sudo apt install docker.io -y

sudo docker swarm init

sudo docker network create -d web_network \
--driver overlay \
--subnet=192.168.100.0/24