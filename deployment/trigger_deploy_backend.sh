#!/bin/bash -x

if [ ! -d ./viz_server ]; then
  git clone https://github.com/AlexeyBeley/viz_server;
  cd ./viz_server
else
  cd ./viz_server
  git pull
fi

cd ./src/backend
CURRENT_CONTAINER=$(docker ps -q -f label=backend)
docker kill $CURRENT_CONTAINER
./deploy.sh
