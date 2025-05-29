from django.urls import path
from WebCompany import views
app_name="WebCompany"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),

    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('DriverRegistration/',views.DriverRegistration,name="DriverRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    
    path('DriverListNew/',views.DriverListNew,name="DriverListNew"),
    path('acceptdriver/<int:aid>',views.acceptdriver,name="acceptdriver"),
    path('rejectdriver/<int:rid>',views.rejectdriver,name="rejectdriver"),
    path('DriverListAccepted/',views.DriverListAccepted,name="DriverListAccepted"),
    path('DriverListRejected/',views.DriverListRejected,name="DriverListRejected"),

    path('VechicleRegistration/',views.VechicleRegistration,name="VechicleRegistration"),
    path('delVechicle/<int:did>',views.delVechicle,name="delVechicle"),

    path('CollectionScheduleDatesEntry/',views.CollectionScheduleDatesEntry,name="CollectionScheduleDatesEntry"),
    path('ScheduleListNew/',views.ScheduleListNew,name="ScheduleListNew"),
    path('deleteschedule/<int:did>',views.deleteschedule,name="deleteschedule"),
    path('acceptschedule/<int:aid>',views.acceptschedule,name="acceptschedule"),
    path('rejectschedule/<int:rid>',views.rejectschedule,name="rejectschedule"),
    path('CollectionScheduleDatesActive/',views.CollectionScheduleDatesActive,name="CollectionScheduleDatesActive"),
    path('CollectionScheduleDatesInactive/',views.CollectionScheduleDatesInactive,name="CollectionScheduleDatesInactive"),

    path('UserRequestForCollection/', views.UserRequestForCollection,name="UserRequestForCollection"),
 

  

]