#!/bin/bash

sudo docker build -t front .
sudo docker run -d -p 80:80 --network internal_network --ip 192.168.1.3 front

#curl http://127.0.0.1/abracadabra