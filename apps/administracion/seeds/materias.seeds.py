from django_seed import Seed
from apps.administracion.models import Subject

seeder = Seed.seeder()

# Define una lista de objetos a crear
objects = [
    {"name": "Matemáticas"},
    {"name": "Lengua y literatura"},
    {"name": "Ciencias Sociales"},
    {"name": "Ciencias Naturales"},
    {"name": "Geografía"},
    {"name": "Biología"}
]

# Agrega los objetos al seeder
seeder.add_entity(Subject, len(objects), objects)

# Crea los objetos
inserted_pks = seeder.execute()

print(f"Creados {len(inserted_pks)} objetos de {Subject.__name__}")