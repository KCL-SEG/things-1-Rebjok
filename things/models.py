from django.db import models
from django.core.validators import MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.PositiveIntegerField(unique=False, validators=[MaxValueValidator(100)])
