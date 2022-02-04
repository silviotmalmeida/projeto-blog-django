#!/bin/bash

echo "Definindo permissoes da pasta de código-fonte..."
docker container exec blog-django chmod 777 -R /root
sleep 1

echo "Parando o container..."
docker-compose down
