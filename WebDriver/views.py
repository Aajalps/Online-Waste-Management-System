from django.shortcuts import render,redirect
from WebGuest.models import *
from WebCompany.models import *
from WebAdmin.models import *
from WebDriver.models import *
# Create your views here.

def homepage(request):
    return render(request,"WebDriver/HomePage.html")

def my_pro(request):
    data=tbl_driver.objects.get(id=request.session["did"])
    return render(request,"WebDriver/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_driver.objects.get(id=request.session["did"])
    if request.method=="POST":
        prodata.driver_name=request.POST.get('txtname')
        prodata.driver_contact=request.POST.get('txtcon')
        prodata.driver_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"WebDriver/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebDriver/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_driver.objects.filter(id=request.session["did"],driver_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_driver.objects.get(id=request.session["did"],driver_password=request.POST.get('txtcurpass'))
                userdata.driver_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"WebDriver/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebDriver/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebDriver/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebDriver/ChangePassword.html")



def CollectionScheduleDatesActive(request):
    prodata=tbl_driver.objects.get(id=request.session["did"])
    userdata = tbl_collectionschedule.objects.filter(collection_status=1,driver=prodata)
    return render(request,"WebDriver/CollectionScheduleDatesListActive.html",{"userdata":userdata})



def WasteCollectionRecordEntry(request):
    ward = tbl_ward.objects.all()
    category = tbl_wastecategory.objects.all()
    if request.method=="POST":
        prodata=tbl_driver.objects.get(id=request.session["did"])
        user = tbl_user.objects.get(id=request.POST.get('sel_user'))
        category = tbl_wastecategory.objects.get(id=request.POST.get('sel_category'))
        tbl_wastecollection.objects.create(category=category,user=user,collection_date=request.POST.get("txtdate"),collection_qty=request.POST.get("txtqty"),driver=prodata)
        return redirect("WebDriver:WasteCollectionRecordEntry")
    else:
        return render(request,"WebDriver/WasteCollectionRecordEntry.html",{"ward":ward,"category":category})


def ajaxuser(request):
    dis = tbl_ward.objects.get(id=request.GET.get("did"))
    place = tbl_user.objects.filter(ward=dis)
    return render(request,"WebDriver/AjaxUser.html",{"placedata":place})


def WasteCollectionRecordList(request):
    prodata=tbl_driver.objects.get(id=request.session["did"])
    userdata = tbl_wastecollection.objects.filter(driver=prodata)
    return render(request,"WebDriver/WasteCollectionRecordList.html",{"userdata":userdata})


def delCollection(request,did):
    tbl_watecollection.objects.get(id=did).delete()
    return redirect("WebDriver:WasteCollectionRecordList")