from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
    
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_ward(models.Model):
    ward_name=models.CharField(max_length=50)


class tbl_wastecategory(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_wasterate(models.Model):
    wasterate_amount=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_wastecategory,on_delete=models.CASCADE)

