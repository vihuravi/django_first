from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Address(models.Model):
    aid = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField(validators=[MinValueValidator(111111),MaxValueValidator(999999)])

    @classmethod
    def get_dummy_address(cls):
        return cls(aid='',city='',state='',pincode='')

class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    salary = models.FloatField()
    role = models.CharField(max_length=30)
    adr = models.ManyToManyField(Address,related_name='emp')

    @classmethod
    def get_dummy_employee(cls):
        return cls(eid='',name='',age='',email='',salary='',role='')