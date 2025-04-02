from django.urls import path # type: ignore
from Guest import views
app_name="Guest"

urlpatterns = [

    path('Login/', views.Login , name='Login'),
    path('UserRegistration/', views.UserRegistration , name='UserRegistration'),
    path('ajaxplace/', views.ajaxplace , name='ajaxplace'),
    path('artist/', views.artist , name='artist'),
    path('deliveryboy/', views.deliveryboy , name='deliveryboy'),

    path('', views.index , name='index'),
    path('about', views.about , name='about'),
    path('gallery', views.gallery , name='gallery'),



    
    

]
