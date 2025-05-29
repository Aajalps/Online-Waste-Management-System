from django.shortcuts import render,redirect
from WebAdmin.models import *
from WebGuest.models import *
from WebCompany.models import *
# Create your views here.

def userRegistration(request):
    district = tbl_ward.objects.all()
    if request.method=="POST":
        place = tbl_ward.objects.get(id=request.POST.get('sel_district'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_houseno=request.POST.get("txtno"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),ward=place)
        return redirect("WebGuest:userRegistration")
    else:
        return render(request,"WebGuest/NewUser.html",{"districtdata":district})


def CompanyRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_company.objects.create(company_name=request.POST.get("txtname"),company_contact=request.POST.get("txtcontact"),company_email=request.POST.get("txtemail"),company_photo=request.FILES.get("fileImage"),company_proof=request.FILES.get("fileProof"),company_password=request.POST.get("txtpwd"),place=place)
        return redirect("WebGuest:CompanyRegistration")
    else:
        return render(request,"WebGuest/CompanyRegistration.html",{"districtdata":district})


def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"WebGuest/AjaxPlace.html",{"placedata":place})

def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()  
        compcount = tbl_company.objects.filter(company_status='1',company_email=request.POST.get("txt_email"),company_password=request.POST.get("txt_password")).count()      
        drcount = tbl_driver.objects.filter(driver_status='1',driver_email=request.POST.get("txt_email"),driver_password=request.POST.get("txt_password")).count()                                  
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("WebUser:homepage")
        elif compcount > 0:
            comp = tbl_company.objects.get(company_email=request.POST.get("txt_email"),company_password=request.POST.get("txt_password"))
            request.session["cid"] = comp.id
            return redirect("WebCompany:homepage")
        elif drcount > 0:
            dr = tbl_driver.objects.get(driver_email=request.POST.get("txt_email"),driver_password=request.POST.get("txt_password"))
            request.session["did"] = dr.id
            return redirect("WebDriver:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            return redirect("WebAdmin:LoadingHomePage")
        else:
            return render(request,"WebGuest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"WebGuest/Login.html")


def Index(request):
    return render(request,"WebGuest/index.html")