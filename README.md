# Índice

- [Sistema Académico](#sistema-académico)
- [Repositorio frontend](#link-al-repositorio-frontend)
- [Configuración Inicial](#configuración-inicial)
  - [Clonar el repositorio](#1-clonar-el-repositorio)
  - [Construcción de imagen docker](#2-construcción-de-imagen-docker)
  - [Levantar los servicios con docker-compose](#3-levantar-los-servicios-con-docker-compose)
  - [Migración de datos de prueba](#4-migración-de-datos-de-prueba)
  - [Acceso a la consola del docker](#para-acceder-a-la-consola-del-docker)
  - [Usuarios de prueba](#-users-de-prueba)

## Sistema Académico

El presente repositorio consiste en una API para gestión y administración de un sistema escolar desarrollado en Python y Django/DRF.

Para las pruebas de desarrollo el docker-compose incluye una imagen de PostgreSQL y una de Portainer para el manejo de los servicios.

##### Link al repositorio frontend
https://github.com/ivangillig/sisacad-ui

<br>

## Configuración Inicial

#### 1. Clonar el repositorio
Clonar el repositorio en la ruta deseada:
```sh
git clone https://gitlab.com/ivan.gillig/sisacad-api
```
Luego acceder a la carpeta del proyecto 
```sh
cd sisacad-api
```

#### 2. Construcción de imagen docker
```sh
sudo docker-compose build
```
#### 3. Levantar los servicios con docker-compose
```sh
sudo docker-compose up
```
#### 4. Migración de datos de prueba
En otra terminal, posicionarse en la ruta principal del proyecto **sisacad-api/** y ejecutar:
```sh
sh load_initial_data.sh
```
#### Para acceder a la consola del docker:
```sh
sudo docker exec -it Sisacad_API sh
```
<br>
<br>

#### \*** Users de prueba
**Admin**
```sh
user: admin@jif.com
pass: admin
```


