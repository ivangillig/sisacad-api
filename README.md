# Sistema Académico

El presente repositorio consiste en una API para gestion y administración de un sistema escolar desarrollado en Python y Django/DRF.

Para las pruebas de desarrollo el docker-compose incluye una imagen de PostgreSQL y una de Portainer para el manejo de los servicios.

## Configuración Inicial

#### 1- Clonar el repositorio
Clonar el repositorio en la ruta deseada:
```sh
git clone https://gitlab.com/ivan.gillig/sisacad-api
```
Luego acceder a la carpeta del proyecto 
```sh
cd sisacad-api
```

#### 2- Construcción de imagen docker
```sh
sudo docker-compose build
```
#### 3- Migración de datos de prueba
Posicionarse en la ruta principal del proyecto **sisacad-api/**
```sh
sh load_initial_data.sh
```
#### 4- Levantar el servicio de docker
```sh
sudo docker-compose up
```
#### Users de prueba
**Admin**
```sh
user: admin@jif.com
pass: admin
```

<br>
<br>

#### Link al repositorio frontend
https://github.com/ivangillig/sisacad-ui

