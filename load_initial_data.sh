#!/bin/bash

python3 manage.py loaddata apps/users/fixtures/users_data.json; \
python3 manage.py loaddata apps/administracion/fixtures/division_data.json;
python3 manage.py loaddata apps/administracion/fixtures/subjects_data.json;