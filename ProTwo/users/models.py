from django.db import models

# Create your models here.
class Names(models.Model):
    name = models.CharField(max_length=40,unique=True)
    lastname = models.CharField(max_length=120,unique=True)
    email = models.EmailField(max_length=120,unique=True)

    def __str__(self):
        return self.name