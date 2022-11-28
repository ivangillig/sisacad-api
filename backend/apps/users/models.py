from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from apps.base.models import BaseModel

from .managers import UserManager

##THIRDPARTY
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    """User model."""

    username = None
    first_name = None
    last_name = None
    email = models.EmailField(('Email institucional'), unique=True)

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        STUDENT = "ALUMNO", "Alumno"
        TEACHER = "DOCENTE", "Docente"
        TUTOR = "TUTOR", "Tutor"

    #base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #asked in console

    objects = UserManager()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class Address(models.Model):
    street = models.CharField('Calle', max_length=20, blank=True, null=True)
    number = models.CharField('Número', max_length=4, blank=True, null=True)
    floor = models.CharField('Piso', max_length=2, blank=True, null=True)
    department = models.CharField('Departamento', max_length=2, blank=True, null=True)
    address_state = models.CharField('Provincia', max_length=2, blank=True, null=True)
    cp = models.CharField('Código Postal', max_length=6, blank=True, null=True)

    class Meta:
        """Meta definition for BaseModel."""

        abstract = True
        verbose_name = 'AddressModel'
        verbose_name_plural = 'AddressModels'
    # class Meta:
    #     verbose_name = 'Dirección'
    #     verbose_name_plural = 'Direcciones'
    #     ordering = ['street']
    
    # def __str__(self):
    #     texto = '{} - {} {}'.format(
    #         self.person.doc_number,
    #         self.street,
    #         self.number,
    #     )
    #     return texto

class Person(Address, BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    doc_number = models.CharField('DNI', max_length=13, unique=True)
    first_name = models.CharField('Primer nombre', max_length=15)
    middle_name = models.CharField('Segundo nombre', max_length=15, blank=True, null=True)
    first_lastname = models.CharField('Primer apellido', max_length=15)
    second_lastname = models.CharField('Segundo apellido', max_length=15, blank=True, null=True)
    personal_email = models.EmailField('Email personal', max_length=40, blank=True, null=True)
    birthday = models.DateField('Fecha de nacimiento', blank=True, null=True)
    birth_place = models.CharField('Lugar de nacimiento', max_length=20, blank=True, null=True)
    nationality = CountryField('Nacionalidad', blank_label='Selecciona un país', null=True)
    CHOICES_GENDER = [
        ('3', 'Masculino'),
        ('4', 'Femenino'),
        ('2', 'Sin genero'),
        ('1', 'Sin especificar'),
    ]
    gender = models.CharField(
        'Género',
        max_length=1,
        choices = CHOICES_GENDER,
        default='Sin especificar',
        null=True,
        )
    phone = models.CharField('Nro de teléfono', max_length=15, blank=True, null=True)
    STATE_CHOICES = [
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viudo/a', 'Viudo/a'),
        ('No aplica', 'No aplica'),
    ]
    marital_status = models.CharField(
        'Estado civil',
        max_length=20,
        choices = STATE_CHOICES,
        default='No aplica',
        null=True,
        )

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['first_name']
    
    def __str__(self):
        texto = '{} {}'.format(
            self.first_name,
            self.first_lastname,
        )
        return texto



