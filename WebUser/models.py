from django.db import models
from WebGuest.models import *

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
   

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_userrequest(models.Model):
    request_date=models.CharField(max_length=500)
    request_message=models.CharField(max_length=500)
    request_postdate=models.DateField(auto_now_add=True)
    request_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)