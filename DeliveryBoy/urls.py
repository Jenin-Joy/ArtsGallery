from django.urls import path
from DeliveryBoy  import views

app_name="DeliveryBoy"
urlpatterns=[
        path('dhomepage/',views.dhomepage,name="dhomepage"),
        path('logout/',views.logout,name="logout"),
        path('deliveryboyprofile/',views.deliveryboyprofile,name="deliveryboyprofile"),
        path('deliveryedit/', views.deliveryedit , name='deliveryedit'),
        path('changedeliveryboypassword/', views.changedeliveryboypassword , name='changedeliveryboypassword'),
        path('complaint/',views.complaint,name="complaint"),

        path('viewbooking/',views.viewbooking,name="viewbooking"),
        path('orderupdation/<int:id>/<int:status>',views.orderupdation,name="orderupdation"),
        path('myorder/',views.myorder,name="myorder"),

        path('viewauctions/', views.viewauctions, name="viewauctions"),
        path('acceptauction/<int:id>/', views.acceptauction, name="acceptauction"),
        path('myauctions/', views.myauctions, name="myauctions"),
        path('auctiondeliveryupdate/<int:id>/<int:status>', views.auctiondeliveryupdate, name="auctiondeliveryupdate"),



]
