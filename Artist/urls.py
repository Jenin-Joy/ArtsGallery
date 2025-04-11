from django.urls import path
from Artist import views
app_name="Artist"

urlpatterns = [
    
    path('artisthomepage/', views.artisthomepage , name='artisthomepage'),
    path('artistprofile/', views.artistprofile , name='artistprofile'),
    path('artistedit/', views.artistedit , name='artistedit'),
    path('changeartistpassword/', views.changeartistpassword , name='changeartistpassword'),
    path('addartwork/', views.addartwork , name='addartwork'),
    path('delartwork/<int:id>', views.delartwork , name='delartwork'),
    path('viewbooking/', views.viewbooking , name='viewbooking'),
    path('artistcomplaint/', views.artistcomplaint , name='artistcomplaint'),
    path('delcomplaint/<int:id>', views.delcomplaint , name='delcomplaint'),
    path('logout/', views.logout , name='logout'),
    path('artistabout', views.artistabout , name='artistabout'),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('chatlist/',views.chatlist,name="chatlist"),


    path('viewevent/',views.viewevent,name="viewevent"),
    path('BookEvent/<int:id>',views.BookEvent,name="BookEvent"),

    path('ticketpayment/<int:id>',views.ticketpayment,name="ticketpayment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),
    path('bookchecking/',views.bookchecking,name="bookchecking"),
    path('tickets/<int:id>',views.tickets,name="tickets"),
    path('cancelbooking/',views.cancelbooking,name="cancelbooking"),

    path('orderupdation/<int:id>/<int:status>',views.orderupdation,name="orderupdation"),



    path('addtoauction/<int:id>', views.addtoauction , name='addtoauction'),
    path('auctionlist/', views.auctionlist , name='auctionlist'),
    path('auctionupdation/<int:id>/<int:status>', views.auctionupdation , name='auctionupdation'),
    path('completedauction/', views.completedauction , name='completedauction'),
    # path('assign_deliveryboy/<int:id>/', views.assign_deliveryboy, name='assign_deliveryboy'),
    # path('assign_deliveryboy_action/<int:auction_id>/<int:delivery_id>/', views.assign_deliveryboy_action, name='assign_deliveryboy_action'),

]
