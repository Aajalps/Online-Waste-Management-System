from django.urls import path,include
from WebAdmin import views
app_name="WebAdmin"
urlpatterns = [


    path('HomePage/',views.LoadingHomePage, name="LoadingHomePage"),
    
    path('District/',views.District, name="District"),
    path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('Updatedis/<int:uid>' , views.Updatedis,name="Updatedis"),


    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),


    path('Ward/',views.Ward, name="Ward"),
    path('DeleteWard/<int:did>',views.DeleteWard,name="DeleteWard"),
    path('UpdateWard/<int:uid>' , views.UpdateWard,name="UpdateWard"),

    path('ComplaintListNew/',views.ComplaintListNew,name="ComplaintListNew"),
    path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
    path('ComplaintSolved/',views.ComplaintSolved,name="ComplaintSolved"),


    path('UserFeedbackNew/',views.UserFeedbackNew,name="UserFeedbackNew"),


    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdminReg/<int:did>', views.delAdminReg,name="delAdminReg"),
    path('adminRegUpdate/<int:eid>',views.adminRegUpdate,name="adminRegUpdate"),

    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),

    path('companyListNew/',views.companyListNew,name="companyListNew"),
    path('acceptcompany/<int:aid>',views.acceptcompany,name="acceptcompany"),
    path('rejectcompany/<int:rid>',views.rejectcompany,name="rejectcompany"),
    path('companyListAccepted/',views.companyListAccepted,name="companyListAccepted"),
    path('companyListRejected/',views.companyListRejected,name="companyListRejected"),

    path('WasteCategory/',views.WasteCategory, name="WasteCategory"),
    path('DeleteWasteCategory/<int:did>',views.DeleteWasteCategory,name="DeleteWasteCategory"),
    path('UpdateWasteCategory/<int:uid>' , views.UpdateWasteCategory,name="UpdateWasteCategory"),


    path('WasteRate/', views.WasteRate,name="WasteRate"),
    path('delWasteRate/<int:did>', views.delWasteRate,name="delWasteRate"),


    
]
