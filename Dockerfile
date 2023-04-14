# Partimos de una base oficial de python
FROM python:3.10

# Crear un directorio para la aplicación
RUN mkdir /sisacad-api

# El directorio de trabajo es desde donde se ejecuta el contenedor al iniciarse
WORKDIR /sisacad-api

# Copiamos todos los archivos del build context al directorio /app del contenedor
ADD . /sisacad-api

# Actualizo el pip
RUN pip install --upgrade pip

# Instalar las dependencias en el contenedor
RUN pip install -r requirements.txt

# Levantar el servidor
CMD python3 manage.py runserver --settings=core.settings.dev




