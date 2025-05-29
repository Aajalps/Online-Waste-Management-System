from django.shortcuts import render,redirect
from WebGuest.models import *
from WebCompany.models import *
from WebUser.models import *

# Create your views here.

def homepage(request):
    return render(request,"WebCompany/HomePage.html")

def my_pro(request):
    data=tbl_company.objects.get(id=request.session["cid"])
    return render(request,"WebCompany/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    if request.method=="POST":
        prodata.company_name=request.POST.get('txtname')
        prodata.company_contact=request.POST.get('txtcon')
        prodata.company_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"WebCompany/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebCompany/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_company.objects.filter(id=request.session["cid"],company_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_company.objects.get(id=request.session["cid"],company_password=request.POST.get('txtcurpass'))
                userdata.company_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"WebCompany/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebCompany/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebCompany/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebCompany/ChangePassword.html")


def DriverRegistration(request):
    district = tbl_district.objects.all()
    prodata=tbl_company.objects.get(id=request.session["cid"])
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_driver.objects.create(company=prodata,driver_name=request.POST.get("txtname"),driver_contact=request.POST.get("txtcontact"),driver_email=request.POST.get("txtemail"),driver_photo=request.FILES.get("fileImage"),driver_proof=request.FILES.get("fileProof"),driver_password=request.POST.get("txtpwd"),place=place)
        return redirect("WebCompany:DriverRegistration")
    else:
        return render(request,"WebCompany/DriverRegistration.html",{"districtdata":district})


def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"WebCompany/AjaxPlace.html",{"placedata":place})


#
def DriverListNew(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    userdata = tbl_driver.objects.filter(driver_status=0,company=prodata)
    return render(request,"WebCompany/DriverListNew.html",{"userdata":userdata})

def acceptdriver(request,aid):
    user = tbl_driver.objects.get(id=aid)
    user.driver_status = 1
    user.save()
    return redirect("WebCompany:homepage")

def rejectdriver(request,rid):
    user = tbl_driver.objects.get(id=rid)
    user.driver_status = 2
    user.save()
    return redirect("WebCompany:homepage")

def DriverListAccepted(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    userdata = tbl_driver.objects.filter(driver_status=1,company=prodata)
    return render(request,"WebCompany/DriverListAccepted.html",{"userdata":userdata})

def DriverListRejected(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    userdata = tbl_driver.objects.filter(driver_status=2,company=prodata)
    return render(request,"WebCompany/DriverListRejected.html",{"userdata":userdata})


#
def VechicleRegistration(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    data = tbl_vehicle.objects.filter(company=prodata)
    if request.method=="POST":
        tbl_vehicle.objects.create(company=prodata,vehicle_name=request.POST.get("txtname"),vehicle_number=request.POST.get("txtregno"),vehicle_photo=request.FILES.get("fileImage"))
        return redirect("WebCompany:VechicleRegistration")
    else:
        return render(request,"WebCompany/VechicleRegistration.html",{"data":data})

def delVechicle(request,did):
    tbl_vehicle.objects.get(id=did).delete()
    return redirect("WebCompany:VechicleRegistration")

#
def CollectionScheduleDatesEntry(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    vdata = tbl_vehicle.objects.filter(company=prodata)
    ddata = tbl_driver.objects.filter(company=prodata)
    wdata = tbl_ward.objects.all()
    if request.method=="POST":
        vehicle = tbl_vehicle.objects.get(id=request.POST.get('sel_vechicle'))
        driver = tbl_driver.objects.get(id=request.POST.get('sel_driver'))
        ward = tbl_ward.objects.get(id=request.POST.get('sel_ward'))
        tbl_collectionschedule.objects.create(company=prodata,collection_date=request.POST.get("txtdate"),collection_time=request.POST.get("txttime"),vehicle=vehicle,driver=driver,ward=ward)
        return redirect("WebCompany:CollectionScheduleDatesEntry")
    else:
        return render(request,"WebCompany/CollectionScheduleDatesEntry.html",{"vdata":vdata,"ddata":ddata,"wdata":wdata})

def ScheduleListNew(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    userdata = tbl_collectionschedule.objects.filter(collection_status=0,company=prodata)
    return render(request,"WebCompany/CollectionScheduleDatesList.html",{"userdata":userdata})

def deleteschedule(request,did):
    tbl_collectionschedule.objects.get(id=did).delete()
    return redirect("WebCompany:homepage")

def acceptschedule(request,aid):
    user = tbl_collectionschedule.objects.get(id=aid)
    user.collection_status = 1
    user.save()
    return redirect("WebCompany:homepage")

def rejectschedule(request,rid):
    user = tbl_collectionschedule.objects.get(id=rid)
    user.collection_status = 2
    user.save()
    return redirect("WebCompany:homepage")

def CollectionScheduleDatesActive(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    userdata = tbl_collectionschedule.objects.filter(collection_status=1,company=prodata)
    return render(request,"WebCompany/CollectionScheduleDatesListActive.html",{"userdata":userdata})

def CollectionScheduleDatesInactive(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    userdata = tbl_collectionschedule.objects.filter(collection_status=2,company=prodata)
    return render(request,"WebCompany/CollectionScheduleDatesListInactive.html",{"userdata":userdata})


def UserRequestForCollection(request):
    data=tbl_userrequest.objects.filter(request_status=0)
    return render(request,"WebCompany/UserRequestForCollection.html",{'data':data})