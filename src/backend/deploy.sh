#!/bin/bash

sudo docker build -t backend .
sudo docker run -d --network internal_network --ip 192.168.1.2 backend
