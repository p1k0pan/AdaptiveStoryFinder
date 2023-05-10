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



class Article(models.Model):
    titel = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    views = models.CharField(max_length=255)
    release_date = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    num_sections = models.IntegerField()
    num_images = models.IntegerField()



    #one_category = 'one_category'
    #two_categories = 'two_categories'

    #TYPE_CHOICES = (
    #    (one_category, 'two_categories'),
    #    (two_categories, 'one_category')
    #)
    #type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=one_category)