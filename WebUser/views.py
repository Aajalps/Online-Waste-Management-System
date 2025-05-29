from django.shortcuts import render,redirect
from WebGuest.models import *
from WebUser.models import *
from WebAdmin.models import *
from WebDriver.models import *

# Create your views here.

def homepage(request):
    return render(request,"WebUser/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"WebUser/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"WebUser/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebUser/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"WebUser/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebUser/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebUser/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebUser/ChangePassword.html")

#
def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("WebUser:POSTComplaint")
    else:
        return render(request,"WebUser/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("WebUser:POSTComplaint")


def UserFeedback(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("WebUser:UserFeedback")
    else:
        return render(request,"WebUser/UserFeedback.html",{"data":data})
   

def delFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("WebUser:UserFeedback")


def CollectionScheduleDatesActive(request):
    userdata = tbl_collectionschedule.objects.filter(collection_status=1)
    return render(request,"WebUser/CollectionScheduleDatesListActive.html",{"userdata":userdata})

def WasteCollectionRecordList(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    userdata = tbl_wastecollection.objects.filter(user=prodata)
    return render(request,"WebUser/WasteCollectionRecordList.html",{"userdata":userdata})


#
def UserRequestForCollection(request):
   
    userid=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_userrequest.objects.filter(user=userid)
    if request.method=="POST":
        datefor=request.POST.get('txtdate')
        message=request.POST.get('txtmsg')
        tbl_userrequest.objects.create(request_date=datefor,request_message=message,user=userid)
        return redirect("WebUser:UserRequestForCollection")
    else:
        return render(request,"WebUser/UserRequestForCollection.html",{'data':data})

def delUserRequest(request,did):
    tbl_userrequest.objects.get(id=did).delete()
    return redirect("WebUser:UserRequestForCollection")