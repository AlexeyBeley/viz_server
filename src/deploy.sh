apt-get update
sudo apt install docker.io

docker network create web_network \
--driver overlay \
--subnet=192.168.100.0/24