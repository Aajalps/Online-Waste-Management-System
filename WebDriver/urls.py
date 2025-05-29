from django.urls import path
from WebDriver import views
app_name="WebDriver"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),

    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('CollectionScheduleDatesActive/',views.CollectionScheduleDatesActive,name="CollectionScheduleDatesActive"),

    path('WasteCollectionRecordEntry/',views.WasteCollectionRecordEntry,name="WasteCollectionRecordEntry"),
    path('AjaxUser/',views.ajaxuser,name="ajaxuser"),
    path('WasteCollectionRecordList/',views.WasteCollectionRecordList,name="WasteCollectionRecordList"),
    path('delCollection/<int:did>',views.delCollection,name="delCollection"),
  

]