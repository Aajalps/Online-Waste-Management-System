from django.urls import path
from WebGuest import views
app_name="WebGuest"

urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('CompanyRegistration/',views.CompanyRegistration,name="CompanyRegistration"),
   
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    
    path('Login/',views.Login,name="Login"),


    path('',views.Index,name="Index"),
]