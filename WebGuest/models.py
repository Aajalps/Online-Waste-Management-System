from django.db import models
from WebAdmin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_houseno=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    ward = models.ForeignKey(tbl_ward, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")

class tbl_company(models.Model):
    company_name=models.CharField(max_length=50)
    company_contact=models.CharField(max_length=50)
    company_email=models.CharField(max_length=50)
    company_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    company_photo = models.FileField(upload_to='Assets/CompanyPhoto/')
    company_proof = models.FileField(upload_to='Assets/CompanyProof/')
    company_status = models.IntegerField(default="0")
    