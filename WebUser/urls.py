from django.urls import path
from WebUser import views
app_name="WebUser"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),

    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),

    path('UserFeedback/', views.UserFeedback, name='UserFeedback'),
    path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),

    path('CollectionScheduleDatesActive/',views.CollectionScheduleDatesActive,name="CollectionScheduleDatesActive"),

     path('WasteCollectionRecordList/',views.WasteCollectionRecordList,name="WasteCollectionRecordList"),

    path('UserRequestForCollection/', views.UserRequestForCollection,name="UserRequestForCollection"),
    path('delUserRequest/<int:did>', views.delUserRequest,name="delUserRequest"),
    

]