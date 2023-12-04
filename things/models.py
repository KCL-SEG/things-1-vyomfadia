from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator


# Create your models here.
class Thing(models.Model):
    """The basic thing model that is required for us to implement."""

    name = models.CharField(unique=True, max_length=30)
    description = models.TextField(null=True, validators=[MaxLengthValidator(120)])
    quantity = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
