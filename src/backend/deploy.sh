#!/bin/bash

sudo docker build -t backend .
sudo docker run -d -p 8000:8000 --network internal_network --ip 192.168.1.2 backend
