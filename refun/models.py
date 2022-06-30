from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=40,null=True)
    designation = models.CharField(max_length=40,null=True)
    exp = models.IntegerField(null=True)
    contactno = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name