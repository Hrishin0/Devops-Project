from django.db import models

# Create your models here.


class Sign(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200, default=" ")
    age = models.IntegerField(default=0)
    description = models.CharField(max_length=400, default= " ")
    image = models.ImageField(upload_to='images/', blank = True, null = True)

    def __str__(self):
        return self.name  + " " 