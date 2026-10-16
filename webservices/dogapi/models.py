from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
    gender = models.CharField(
      max_length=1, choices=GenderChoices.choices, default=GenderChoices.MALE
    )
    color = models.CharField(max_length=20, default = 'unknown')
    favoritefood = models.CharField(max_length=100, default = 'unknown')
    favoritetoy = models.CharField(max_length=100, default = 'unknown')

    def __str__(self):
        return self.name

class Breed(models.Model):
    breed = models.CharField(max_length=100)
    class Size(models.TextChoices):
            SMALL = "small", "Small"
            MEDIUM = "medium", "Medium"
            LARGE = "large", "Large"
    size = models.CharField(
        max_length=10, 
        choices=Size.choices, 
        default=Size.MEDIUM
    )
    friendliness = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)])                        
    trainability = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    excerciseneeds = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self):
            return self.breed