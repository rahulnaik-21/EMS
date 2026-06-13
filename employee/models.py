from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):

    name = models.CharField(max_length=100)

    salary = models.IntegerField()

    designation = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    
# This controls how data appears in admin panel
    def __str__(self):
        return self.name
