# Awesome Products API

[![GitHub](https://img.shields.io/github/license/mdcg/awesome-products-api.svg)](https://github.com/mdcg/awesome-products-api/blob/master/LICENSE)

:hammer_and_wrench: *A simple API written in DRF*

## First steps

First of all, make sure you have Docker and Docker Compose installed on your machine. If you do not have it, here are the links for you to install them:

* [Install Docker (v17.12)](https://docs.docker.com/v17.12/install/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)


To initialize the application, run the following command:

```shell
$ docker-compose up
```

## Accessing the Docker container

If you need to access the application container, either to manually perform some migration or anything, use the following commands:

```shell
$ docker ps
```

After executing this command, you will have access to the ID (a hexadecimal sequence displayed in the first column) and the name of the container (displayed in the final column). Copy one of the two and run the following command:

```shell
$ docker exec -it <name or container_id> bash
```

This will let you run arbitrary commands inside an existing container.

## Debugging

If you need to debug the application, before adding 'pdb' to your code, run the following command:

```shell
$ docker attach <name or container_id>
```

If you do not know how to access the name or the id of the container, go to 'Accessing the Docker container'.