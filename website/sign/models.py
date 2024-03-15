from django.db import models

# Create your models here.

class Sign(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return " Welcome " + self.name