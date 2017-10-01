from django.db import models

class List(models.Model):
    name=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    roll_no=models.CharField(max_length=200)
    date_of_birth=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    def __str__(self):
        return (self.name)