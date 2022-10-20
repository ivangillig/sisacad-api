#!/bin/bash -xe

python -c <<EOF |
from django.db import IntegrityError
try:
    python3 manage.py install_labels
except IntegrityError:
    print(“Already installed”)
EOF
python3 manage.py migrate # Apply database migrations
if [ “$DJANGO_SUPERUSER_USERNAME” ]
then
    python manage.py createsuperuser \
        — noinput \
        — username $DJANGO_SUPERUSER_USERNAME \
        — email $DJANGO_SUPERUSER_EMAIL
fi
$@
#python3 manage.py runserver 0.0.0.0:8000