#!/bin/bash

echo "Definindo permissoes da pasta de código-fonte..."
docker container exec blog-django chmod 777 -R /root
sleep 1

echo "Aplicando as migrations..."
docker container exec -it blog-django python3 /root/manage.py migrate

