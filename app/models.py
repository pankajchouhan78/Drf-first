from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30)
    auther = models.CharField(max_length=30)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)

    