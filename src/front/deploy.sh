#!/bin/bash

sudo docker build -t front .
sudo docker run -d -p 80:80 --network internal_network --ip 192.168.1.3 -l front front

#apt-get update
#apt-get install apache2-utils -y

##/etc/nginx/.htpasswd
#Aa123456!
#htpasswd -c /etc/nginx/.htpasswd admin
#1234
#htpasswd /etc/nginx/.htpasswd user

#apt-get install curl -y
#curl http://127.0.0.1/abracadabra
#curl -i -H 'Content-Type: application/json' http://192.168.1.2:8000/abracadabra

