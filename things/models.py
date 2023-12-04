from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Thing(models.Model):
    """The basic thing model that is required for us to implement."""

    name = models.CharField(unique=True, max_length=30)
    description = models.TextField(max_length=120, null=True)
    quantity = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(1)])
