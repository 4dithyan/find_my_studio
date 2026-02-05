from django.db import models
from Adminapp.models import Tbl_category
from Guestapp.models import Tbl_studio


# Create your models here.
class Tbl_work(models.Model):
    workid = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Tbl_category,on_delete=models.CASCADE)
    workname = models.CharField(max_length=25)
    description = models.CharField(max_length=400)
    studioid = models.ForeignKey(Tbl_studio,on_delete=models.CASCADE,default='')
    workimg = models.ImageField(default='')
    

class Tbl_workimage(models.Model):
    workimageid = models.AutoField(primary_key=True)
    work_id = models.ForeignKey(Tbl_work,on_delete=models.CASCADE)
    image1= models.ImageField()
    image2= models.ImageField(default='')
    image3= models.ImageField(default='')
    image4= models.ImageField(default='')
    image5= models.ImageField(default='')
    image6= models.ImageField(default='')
  
class Tbl_package(models.Model):
    packageid = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Tbl_category,on_delete=models.CASCADE)
    packagename = models.CharField(max_length=25)
    description = models.CharField(max_length=400)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    studioid = models.ForeignKey(Tbl_studio,on_delete=models.CASCADE,default='')
    

