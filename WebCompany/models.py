from django.db import models

from WebGuest.models import *
from WebAdmin.models import *
from WebCompany.models import *

# Create your models here.

class tbl_driver(models.Model):
    driver_name=models.CharField(max_length=50)
    driver_contact=models.CharField(max_length=50)
    driver_email=models.CharField(max_length=50)
    driver_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    company = models.ForeignKey(tbl_company, on_delete=models.CASCADE)
    driver_photo = models.FileField(upload_to='Assets/CompanyPhoto/')
    driver_proof = models.FileField(upload_to='Assets/CompanyProof/')
    driver_status = models.IntegerField(default="0")

class tbl_vehicle(models.Model):
    vehicle_name=models.CharField(max_length=50)
    vehicle_number=models.CharField(max_length=50)
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE,null=True)
    vehicle_photo = models.FileField(upload_to='Assets/VechiclePhoto/')


class tbl_collectionschedule(models.Model):
    collection_date=models.CharField(max_length=50)
    collection_time=models.CharField(max_length=50)   
    collection_status = models.IntegerField(default="0")
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE,null=True)
    driver=models.ForeignKey(tbl_driver,on_delete=models.CASCADE,null=True)
    vehicle=models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE,null=True)
    ward=models.ForeignKey(tbl_ward,on_delete=models.CASCADE,null=True)
   
   
    

