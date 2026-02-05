from django.db import models
from Adminapp.models import tbl_location

# Create your models here.
class Tbl_login(models.Model):
    loginid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    status = models.CharField(max_length=25,default='')

from Guestapp.models import Tbl_login
class Tbl_studio(models.Model):
    studioid = models.AutoField(primary_key=True)
    studioname = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.BigIntegerField()
    landmark = models.CharField(max_length=25)
    idproof=models.ImageField()
    simage=models.ImageField(default='')
    pincode=models.BigIntegerField()
    locationid=models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    regdate=models.DateField(auto_now_add=True)
    loginid=models.ForeignKey(Tbl_login,on_delete=models.CASCADE)

class Tbl_customer(models.Model):
    customerid = models.AutoField(primary_key=True)
    customername = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.BigIntegerField()
    pincode=models.BigIntegerField()
    locationid=models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    regdate=models.DateField(auto_now_add=True)
    loginid=models.ForeignKey(Tbl_login,on_delete=models.CASCADE)