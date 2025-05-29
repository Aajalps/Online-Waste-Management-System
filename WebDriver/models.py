from django.db import models
# from WebAdmin.models import *
# from WebGuest.models import *
from WebCompany.models import *

# Create your models here.
class tbl_wastecollection(models.Model):
    collection_date=models.CharField(max_length=50)
    collection_qty=models.CharField(max_length=50)   
    category=models.ForeignKey(tbl_wastecategory,on_delete=models.CASCADE,null=True)
    driver=models.ForeignKey(tbl_driver,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
  
   