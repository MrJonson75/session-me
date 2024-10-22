from django.db import models


# Create your models here.


class Part(models.Model):
    brand = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

