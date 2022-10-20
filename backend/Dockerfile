# Partimos de una base oficial de python
FROM python:3.10
  RUN mkdir /sistema_academico
# El directorio de trabajo es desde donde se ejecuta el contenedor al iniciarse
 WORKDIR /sistema_academico

# Copiamos todos los archivos del build context al directorio /app del contenedor
 ADD . /sistema_academico

# Actualizo el pip
RUN pip install --upgrade pip

# Ejecutamos pip para instalar las dependencias en el contenedor
RUN pip install -r requirements.txt

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]




