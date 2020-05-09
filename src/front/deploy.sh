#!/bin/bash

sudo docker build -t front .
#sudo docker run -d -p 80:80 --network internal_network --ip 192.168.1.3 front


sudo docker run -d -p 80:80 --network internal_network --ip 192.168.1.3 $PWD/front_config.conf:/etc/nginx/conf.d/front_config.conf front


#apt-get update
#apt-get install curl -y
#curl http://127.0.0.1/abracadabra
#curl -i -H 'Content-Type: application/json' http://192.168.1.2:8000/abracadabra