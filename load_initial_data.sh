#!/bin/bash

#Usuarios
python3 manage.py loaddata apps/users/fixtures/users_data.json; \
python3 manage.py loaddata apps/users/fixtures/persons_data.json;


#Administración
python3 manage.py loaddata apps/administracion/fixtures/division_data.json;
python3 manage.py loaddata apps/administracion/fixtures/subjects_data.json;
python3 manage.py loaddata apps/administracion/fixtures/specialities_data.json;
python3 manage.py loaddata apps/administracion/fixtures/levels_data.json;
python3 manage.py loaddata apps/administracion/fixtures/grades_data.json;

#Alumnos
python3 manage.py loaddata apps/alumnos/fixtures/students_data.json;