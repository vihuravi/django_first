from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.FloatField()
    active = models.CharField(max_length=5,default='Y')
    # email = models.CharField(max_length=30)
    # role = models.CharField(max_length=30)

    @classmethod
    def get_dummy_employee(cls):
        return cls(eid='',name='',age='',salary='')