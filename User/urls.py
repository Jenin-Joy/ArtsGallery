from django.urls import path
from  User import views
app_name="User"
urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('viewartwork/',views.viewartwork,name="viewartwork"),
    path('viewevent/',views.viewevent,name="viewevent"),
    path('artist/<int:id>',views.artist,name="artist"),
    path('bookingartwork/<int:id>',views.bookingartwork,name="bookingartwork"),
    path('mybooking/',views.mybooking,name="mybooking"),
    path('BookEvent/<int:id>',views.BookEvent,name="BookEvent"),
    path('feedback/',views.feedback,name="feedback"),
    path('usercomplaint/',views.usercomplaint,name="usercomplaint"),
    path('delcomplaint/<int:id>',views.delcomplaint,name="delcomplaint"),
    path('logout/',views.logout,name="logout"),

    path('payment/<int:id>',views.payment,name="payment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),
    
    path('ticketpayment/<int:id>',views.ticketpayment,name="ticketpayment"),
    path('tickets/<int:id>',views.tickets,name="tickets"),
    path('cancelbooking/',views.cancelbooking,name="cancelbooking"),
    path('bookchecking/',views.bookchecking,name="bookchecking"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),
    
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('viewauctionlist/',views.viewauctionlist,name="viewauctionlist"),
    path('auction/<int:id>',views.auction,name="auction"),
    path('ajaxplacebid/',views.ajaxplacebid,name="ajaxplacebid"),
    path('ajaxgetbid/',views.ajaxgetbid,name="ajaxgetbid"),
    path('ajaxclosebid/',views.ajaxclosebid,name="ajaxclosebid"),
    path('ajaxgettimmer/',views.ajaxgettimmer,name="ajaxgettimmer"),

    path('myauction/',views.myauction,name="myauction"),
    path('auctionpayment/<int:id>',views.auctionpayment,name="auctionpayment"),
]
