from django.db import models

# Create your models here.
class Crud(models.Model):
    slno=models.IntegerField()
    itemname=models.CharField(max_length=250)
    description=models.TextField()
   
   
    def __str__(self):
          return self.itemname