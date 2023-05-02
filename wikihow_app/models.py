from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = (
        (1, 'male'),
        (0, 'female'),
    )
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    id_card = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    temperature = models.FloatField()

    class Meta:
        permissions = ()