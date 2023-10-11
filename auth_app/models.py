from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    mob_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    contacts_number = models.ManyToManyField('self', blank=True)
    spam_cell_numbers = models.ManyToManyField('self', blank=True, symmetrical=False)