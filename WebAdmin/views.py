from django.shortcuts import render,redirect
from WebAdmin.models import *
from WebGuest.models import *
from WebUser.models import *
from datetime import date
# Create your views here.

def LoadingHomePage(request):
    return render(request,"WebAdmin/HomePage.html")


def District(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("txt_district"))
        return redirect("WebAdmin:District")
    else:
        return render(request,"WebAdmin/District.html",{"District":data})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("WebAdmin:District")

def Updatedis(request,uid):
    dis=tbl_district.objects.get(id=uid)
    if request.method=="POST":
        dis.district_name=request.POST.get("txt_district")
        dis.save()
        return redirect("WebAdmin:District")
    else:
        return render(request,"WebAdmin/District.html",{"disdata":dis})
        


          
def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"WebAdmin/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("WebAdmin:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"WebAdmin\Place.html",{"editdata":editdata,"districtdata":district})


def Ward(request):
    data=tbl_ward.objects.all()
    if request.method=="POST":
        tbl_ward.objects.create(ward_name=request.POST.get("txt_district"))
        return redirect("WebAdmin:Ward")
    else:
        return render(request,"WebAdmin/Ward.html",{"District":data})

def DeleteWard(request,did):
    tbl_ward.objects.get(id=did).delete()
    return redirect("WebAdmin:Ward")

def UpdateWard(request,uid):
    dis=tbl_ward.objects.get(id=uid)
    if request.method=="POST":
        dis.ward_name=request.POST.get("txt_district")
        dis.save()
        return redirect("WebAdmin:Ward")
    else:
        return render(request,"WebAdmin/Ward.html",{"disdata":dis})



def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"WebAdmin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"WebAdmin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"WebAdmin/UserListRejected.html",{"userdata":userdata})

#
def companyListNew(request):
    userdata = tbl_company.objects.filter(company_status=0)
    return render(request,"WebAdmin/CompanyListNew.html",{"userdata":userdata})

def acceptcompany(request,aid):
    user = tbl_company.objects.get(id=aid)
    user.company_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectcompany(request,rid):
    user = tbl_company.objects.get(id=rid)
    user.company_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def companyListAccepted(request):
    userdata = tbl_company.objects.filter(company_status=1)
    return render(request,"WebAdmin/CompanyListAccepted.html",{"userdata":userdata})

def companyListRejected(request):
    userdata = tbl_company.objects.filter(company_status=2)
    return render(request,"WebAdmin/CompanyListRejected.html",{"userdata":userdata})




def ComplaintListNew(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    return render(request,"WebAdmin/ComplaintListNew.html",{'userComplaint':userComplaint})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("WebAdmin:LoadingHomePage")
    else:
        return render(request,"WebAdmin/ComplaintListReply.html",{'complaint':complaint})
    
def ComplaintSolved(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"WebAdmin/ComplaintListSolved.html",{'userComplaint':userComplaint})
    

def UserFeedbackNew(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"WebAdmin/UserFeedBack.html",{'data':data})



def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd)
        return redirect("WebAdmin:adminInsertSelect")
    else:
        return render(request,"WebAdmin/AdminRegistration.html",{'data':data})

def delAdminReg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("WebAdmin:adminInsertSelect")

def adminRegUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("WebAdmin:adminInsertSelect")
    else:
        return render(request,"WebAdmin\AdminRegistration.html",{"editdata":editdata})


def WasteCategory(request):
    data=tbl_wastecategory.objects.all()
    if request.method=="POST":
        tbl_wastecategory.objects.create(category_name=request.POST.get("txt_district"))
        return redirect("WebAdmin:WasteCategory")
    else:
        return render(request,"WebAdmin/WasteCategory.html",{"District":data})

def DeleteWasteCategory(request,did):
    tbl_wastecategory.objects.get(id=did).delete()
    return redirect("WebAdmin:WasteCategory")

def UpdateWasteCategory(request,uid):
    dis=tbl_wastecategory.objects.get(id=uid)
    if request.method=="POST":
        dis.category_name=request.POST.get("txt_district")
        dis.save()
        return redirect("WebAdmin:WasteCategory")
    else:
        return render(request,"WebAdmin/WasteCategory.html",{"disdata":dis})

def WasteRate(request):
    categroy = tbl_wastecategory.objects.all()
    data=tbl_wasterate.objects.all()
    if request.method=="POST":
        rate=request.POST.get('txtname')
        categroy = tbl_wastecategory.objects.get(id=request.POST.get('sel_district'))
        tbl_wasterate.objects.create(wasterate_amount=rate,category=categroy)
        return redirect("WebAdmin:WasteRate")
    else:
        return render(request,"WebAdmin/WasteRate.html",{'data':data,"categroy":categroy})

def delWasteRate(request,did):
    tbl_wasterate.objects.get(id=did).delete()
    return redirect("WebAdmin:WasteRate")

