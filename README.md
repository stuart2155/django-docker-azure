# django-docker-azure

Django + Docker + Azure 101

_Notes for me_

    docker build -t django01 .
    docker run -p 8888:80 django01
    docker tag django01 django2155.azurecr.io\django01
    docker push django2155.azurecr.io/django01
    az acr update -n django2155 --admin-enabled true
