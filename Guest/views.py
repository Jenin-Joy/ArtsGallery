from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
def index(request):
       return render(request,"Guest/index.html")

def about(request):
       return render(request,"Guest/about.html")

def gallery(request):
       return render(request,"Guest/gallery.html")

def Login(request):
        if request.method == "POST":
                 email = request.POST.get("txtemail")
                 password = request.POST.get("pass")
                 usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
                 artistcount = tbl_artist.objects.filter(artist_email=email,artist_password=password).count()
                 deliveryboycount = tbl_deliveryboy.objects.filter(deliveryboy_email=email,deliveryboy_password=password).count()
                 admincount = tbl_Adminreg.objects.filter(Adminreg_Email=email,Adminreg_password=password).count()


                 if usercount > 0:
                        user = tbl_user.objects.get(user_email=email,user_password=password)
                        if user.user_status == 0:
                            return render(request, "Guest/Login.html",{"msg":"Your Registration is pending Thank you.."})
                        elif user.user_status == 2:
                            return render(request, "Guest/Login.html",{"msg":"Your Registration is rejected Thank you.."})
                        else:
                            request.session["uid"] = user.id
                            return redirect("User:homepage")
                 
                 elif artistcount > 0:
                        artist = tbl_artist.objects.get(artist_email=email,artist_password=password)
                        if artist.artist_status == 0:
                            return render(request, "Guest/Login.html",{"msg":"Your Registration is pending Thank you.."})
                        elif artist.artist_status == 2:
                            return render(request, "Guest/Login.html",{"msg":"Your Registration is rejected Thank you.."})
                        else:
                            request.session["aid"] = artist.id
                            return redirect("Artist:artisthomepage")
                        
                 elif deliveryboycount > 0:
                        deliveryboy = tbl_deliveryboy.objects.get(deliveryboy_email=email,deliveryboy_password=password)
                        if deliveryboy.deliveryboy_status == 0:
                            return render(request, "Guest/Login.html",{"msg":"Your Registration is pending Thank you.."})
                        elif deliveryboy.deliveryboy_status == 2:
                            return render(request, "Guest/Login.html",{"msg":"Your Registration is rejected Thank you.."})
                        else:
                            request.session["did"] = deliveryboy.id
                            return redirect("DeliveryBoy:dhomepage")
                 
                 elif admincount > 0:
                        admin = tbl_Adminreg.objects.get(Adminreg_Email=email,Adminreg_password=password)
                        request.session["adid"] = admin.id
                        return redirect("Admin:adminhomepage")
                 else:
                        return render(request, 'Guest/Login.html',{"msg":"Invalid Email or Password"})
        else:
               return render(request, 'Guest/Login.html')

def UserRegistration(request):
        dis = tbl_district.objects.all()
        if request.method == "POST":
               tbl_user.objects.create(user_name=request.POST.get("txtname"),
                                  user_email=request.POST.get("txtemail"),
                                  user_contact=request.POST.get("txtcontact"),
                                  user_address=request.POST.get("txtaddress"),
                                  user_password=request.POST.get("pass"),
                                  user_photo=request.FILES.get("txtphoto"),
                                   place=tbl_place.objects.get(id=request.POST.get("place")))
               return redirect("Guest:UserRegistration")
        else:
               return render(request, 'Guest/UserRegistration.html',{"district":dis})

def ajaxplace(request):
    place = tbl_place.objects.filter(district = request.GET.get("did"))
    return render (request, 'Guest\AjaxPlace.html',{"place":place})



def artist(request):
        dis = tbl_district.objects.all()
        if request.method == "POST":
               tbl_artist.objects.create(artist_name=request.POST.get("txtname"),
                                  artist_email=request.POST.get("txtemail"),
                                  artist_contact=request.POST.get("txtcontact"),
                                  artist_address=request.POST.get("txtaddress"),
                                   artist_photo=request.FILES.get("txtphoto"),
                                  artist_proof=request.FILES.get("txtproof"),
                                    artist_password=request.POST.get("pass"),
                                   place=tbl_place.objects.get(id=request.POST.get("place")))
               return redirect("Guest:artist")
        else:
               return render(request, 'Guest/Artist.html',{"district":dis})
        
def deliveryboy(request):
        dis = tbl_district.objects.all()
        if request.method == "POST":
               tbl_deliveryboy.objects.create(deliveryboy_name=request.POST.get("txtname"),
                                  deliveryboy_email=request.POST.get("txtemail"),
                                  deliveryboy_contact=request.POST.get("txtcontact"),
                                  deliveryboy_address=request.POST.get("txtaddress"),
                                  deliveryboy_photo=request.FILES.get("txtphoto"),
                                  deliveryboy_proof=request.FILES.get("txtproof"),
                                  deliveryboy_password=request.POST.get("pass"),
                                   place=tbl_place.objects.get(id=request.POST.get("place")))
               return redirect("Guest:deliveryboy")
        else:
               return render(request, 'Guest/DeliveryBoy.html',{"district":dis})