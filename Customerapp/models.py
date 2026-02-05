from django.db import models
from Studioapp.models import Tbl_package
from Guestapp.models import Tbl_customer


# Create your models here.
class Tbl_request(models.Model):
    requestid = models.AutoField(primary_key=True)
    packageid=models.ForeignKey(Tbl_package,on_delete=models.CASCADE)
    requireddate = models.DateField()
    noofdays = models.BigIntegerField()
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=25)
    remark = models.CharField(max_length=100)
    customerid=models.ForeignKey(Tbl_customer,on_delete=models.CASCADE)
    aamount = models.DecimalField(max_digits=8,decimal_places=2,null=True)

class Tbl_payment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    iamount = models.DecimalField(max_digits=8,decimal_places=2)
    tamount = models.DecimalField(max_digits=8,decimal_places=2)
    camount = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    status = models.CharField(max_length=25)
    requestid=models.ForeignKey(Tbl_request,on_delete=models.CASCADE)
    paymentdate = models.DateField(auto_now_add=True)

class Tbl_feedback(models.Model):
    feedbackid=models.AutoField(primary_key=True)
    description=models.CharField(max_length=100)
    rating=models.IntegerField()
    customerid=models.ForeignKey(Tbl_customer,on_delete=models.CASCADE)
    packageid=models.ForeignKey(Tbl_package,on_delete=models.CASCADE)