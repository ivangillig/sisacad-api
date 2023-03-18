from django_seed import Seed
from apps.administracion.models import Level

seeder = Seed.seeder()

# Define una lista de objetos a crear
objects = [
    {"name": "Inicial"},
    {"name": "Primario"},
    {"name": "Secundario"}
]

# Agrega los objetos al seeder
seeder.add_entity(Level, len(objects), objects)

# Crea los objetos
inserted_pks = seeder.execute()

print(f"Creados {len(inserted_pks)} objetos de {Level.__name__}")