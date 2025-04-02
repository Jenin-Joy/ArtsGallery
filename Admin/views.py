from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Artist.models import *
from User.models import *



# Create your views here.
def logout(request):
      del request.session["adid"]
      return redirect('Guest:index')

def Add(request):
    if request.method=='POST':
        num1=int(request.POST.get('FirstNumber'))
        num2=int(request.POST.get('SecondNumber'))
        result=num1+num2
        return render(request, 'Admin/Add.html',{'res':result})
    else:
        return render(request, 'Admin/Add.html')
    
def Largest(request):
    if request.method=='POST':
        num1=int(request.POST.get('FirstNumber'))
        num2=int(request.POST.get('SecondNumber'))
        if num1>num2:
            result=num1
        else:
            result=num2    
        return render(request, 'Admin/Largest.html',{'res':result})
    else:
        return render(request, 'Admin/Largest.html')
    
def calculator(request):
    if request.method=='POST':
        num1=int(request.POST.get('FirstNumber'))
        num2=int(request.POST.get('SecondNumber'))
        button=request.POST.get('CHECK')

        if button=='+':
            result=num1+num2
        elif button=='-':
            result=num1-num2
        elif button=='*':
            result=num1*num2 
        elif button=='/':
            result=num1/num2 
        return render(request, 'Admin/calculator.html',{'res':result})
    else:
        return render(request, 'Admin/calculator.html')
    
def reg(request):
    if request.method=='POST':
        FirstName=str(request.POST.get('fname'))
        LastName=str(request.POST.get('Lname'))
        name=FirstName+" "+LastName
        Gender=request.POST.get('gender')
        Address=request.POST.get('txtaddress')
        Contact=request.POST.get('txtcontact')
        District=request.POST.get('district')
   
        return render(request, 'Admin/reg.html',{'name':name,'Gender':Gender,'Address':Address,'Contact':Contact,'District':District,})
    else:
        return render(request, 'Admin/reg.html')
    
def district(request):
        return render(request, 'Admin/district.html')

def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get("district")
        tbl_district.objects.create(
            district_name=district
        )
        return render(request,"Admin/District.html",{'msg':"Data Inserted SuccessFully"})
    else:
        return render(request, 'Admin/District.html',{'district':dis})
    
def editdistrict(request, id):
    district = tbl_district.objects.get(id=id)
    if request.method=="POST":
        district.district_name = request.POST.get("district")
        district.save()
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/district.html',{"disdata":district})    
    

def category(request):
    cat=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("category")
        tbl_category.objects.create(
            category_name=category
        )
        return render(request,"Admin/category.html",{'msg':"Data Inserted SuccessFully"})
    else:
        return render(request, 'Admin/category.html',{'category':cat})
    
def editcategory(request, id):
    category = tbl_category.objects.get(id=id)
    if request.method=="POST":
        category.category_name = request.POST.get("category")
        category.save()
        return redirect("Admin:category")
    else:
        return render(request, 'Admin/category.html',{"catdat":category})    
    
def delcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect('Admin:category')

def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect('Admin:district')

def Adminreg(request):
    adm=tbl_Adminreg.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        mail=request.POST.get("mail")
        password=request.POST.get("pass")
        tbl_Adminreg.objects.create(
            Adminreg_name=name,
            Adminreg_Email=mail,
            Adminreg_password=password
        )
        return render(request,"Admin/Adminreg.html",{'msg':"Data Inserted SuccessFully",'Adminreg':adm})
    else:
        return render(request, 'Admin/Adminreg.html',{'Adminreg':adm})
    
def delAdminreg(request,id):
    tbl_Adminreg.objects.get(id=id).delete()
    return redirect('Admin:Adminreg')

def editAdminreg(request, id):
    Adminreg = tbl_Adminreg.objects.get(id=id)
    if request.method=="POST":
        Adminreg.Adminreg_name = request.POST.get("name")
        Adminreg.Adminreg_Email = request.POST.get("mail")
        Adminreg.Adminreg_password = request.POST.get("pass")
        Adminreg.save()
        return redirect("Admin:Adminreg")
    else:
        return render(request, 'Admin/Adminreg.html',{"Admindata":Adminreg})  
    


def place(request):
     dis = tbl_district.objects.all()
     pla = tbl_place.objects.all()

     if request.method=="POST":
         district = tbl_district.objects.get(id=request.POST.get("District"))
         tbl_place.objects.create(place_name=request.POST.get("place"),
                                  district=district)
         return redirect("Admin:place")
     else:
        return render(request, 'Admin/Place.html',{"district":dis,'place':pla})
     
def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect('Admin:place')

def editplace(request, id):
    dis = tbl_district.objects.all()
    place = tbl_place.objects.get(id=id)
    if request.method=="POST":
        place.district = tbl_district.objects.get(id=request.POST.get("District"))
        place.place_name = request.POST.get("place")
        place.save()
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html',{"placedata":place,"district":dis,})

def Subcategory(request):
     cat = tbl_category.objects.all()
     sub = tbl_subcategory.objects.all()

     if request.method=="POST":
         category = tbl_category.objects.get(id=request.POST.get("category"))
         tbl_subcategory.objects.create(Subcategory_name=request.POST.get("subcategory"),
                                  category=category)
         return redirect("Admin:Subcategory")
     else:
        return render(request, 'Admin/Subcategory.html',{"subcategory":sub,'category':cat})
     
def delsub(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect('Admin:Subcategory')

def editSubcategory(request, id):
    cat = tbl_category.objects.all()
    sub = tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        sub.category = tbl_category.objects.get(id=request.POST.get("category"))
        sub.Subcategory_name = request.POST.get("subcategory")
        sub.save()
        return redirect("Admin:Subcategory")
    else:
        return render(request, 'Admin/Subcategory.html',{"subdata":sub,"category":cat,})
    

def verification(request):
    user=tbl_user.objects.all
    return render(request, 'Admin/UserVerification.html',{'user':user})

def deluser(request,id):
    tbl_user.objects.get(id=id).delete()
    return redirect('Admin:verification')

def useraccept(request,id):
    user = tbl_user.objects.get(id=id)
    user.user_status = 1
    user.save()
    return redirect("Admin:verification")

def userreject(request,id):
    user = tbl_user.objects.get(id=id)
    user.user_status = 2
    user.save()
    return redirect("Admin:verification")

def product(request):
    cate = tbl_category.objects.all()
    if request.method == "POST":
        tbl_product.objects.create(product_name=request.POST.get("txtname"),
                                   product_price=request.POST.get("txtprice"),
                                  product_details=request.POST.get("txtdetails"),
                                  product_photo=request.POST.get("txtphoto"),
                                  subcategory=tbl_subcategory.objects.get(id=request.POST.get("subcategory")))
        return redirect("Admin:Product")
    else:
        return render(request, 'Admin/Product.html',{"category":cate})
        
def ajaxsubcategory(request):
    sub = tbl_subcategory.objects.filter(category = request.GET.get("did"))
    return render (request, 'Admin\AjaxSubCategory.html',{"":sub})

def newartist(request):
    if 'adid' in request.session:
        artist=tbl_artist.objects.all
        return render(request, 'Admin/NewArtist.html',{'artist':artist})
    else:
        return redirect('Guest:Login') 

def artistaccept(request,id):
    artist = tbl_artist.objects.get(id=id)
    artist.artist_status = 1
    artist.save()
    return redirect("Admin:newartist")

def artistreject(request,id):
    artist = tbl_artist.objects.get(id=id)
    artist.artist_status = 2
    artist.save()
    return redirect("Admin:newartist")

def acceptedartist(request):
    if 'adid' in request.session:
        artists = tbl_artist.objects.filter(artist_status = 1)
        return render(request, 'Admin/AcceptedArtist.html',{ 'artist':artists})
    else:
        return redirect('Guest:Login') 

def rejectedartist(request):
    if 'adid' in request.session:
        artists = tbl_artist.objects.filter(artist_status = 2)
        return render(request, 'Admin/RejectedArtist.html',{ 'artist':artists})
    else:
        return redirect('Guest:Login') 

def adminhomepage(request):
    if 'adid' in request.session:
        userdata=tbl_user.objects.all()
        artistdata=tbl_artist.objects.all()
        complaintdata=tbl_complaint.objects.all()
        complaintdat=tbl_complaint.objects.filter(complaint_status=0)

        feedbackdata=tbl_feedback.objects.all()
        artworkdata=tbl_artwork.objects.all()
        eventdata=tbl_event.objects.all()
        deldata=tbl_deliveryboy.objects.all()

        ucount=userdata.count()
        acount=artistdata.count()
        comcount=complaintdata.count()
        replycom=complaintdat.count()
        feedcount=feedbackdata.count()
        artworkcount=artworkdata.count()
        eventcount=eventdata.count()
        delcount=deldata.count()



        return render(request, 'Admin/AdminHomePage.html',{'ucount':ucount,'acount':acount,'comcount':comcount,'feedcount':feedcount,'artworkcount':artworkcount,'eventcount':eventcount,'delcount':delcount,'replycom':replycom})
    else:
        return redirect('Guest:Login') 

def addevent(request):
    if 'adid' in request.session:
        event = tbl_event.objects.all()
        if request.method == "POST":
               tbl_event.objects.create(event_name=request.POST.get("txtname"),
                                        event_description=request.POST.get("txtdescription"),
                                        event_count=request.POST.get("txtpersoncount"),
                                        event_todate=request.POST.get("txtdate"),
                                        event_price=request.POST.get("txtprice")),
               return redirect("Admin:addevent")
        else:
               return render(request, 'Admin/AddEvent.html',{"event":event})
    else:
        return redirect('Guest:Login') 

def delevent(request,id):
    tbl_event.objects.get(id=id).delete()
    return redirect('Admin:addevent')

def viewfeedback(request):
    if 'adid' in request.session:
        feedback=tbl_feedback.objects.all
        return render(request, 'Admin/ViewFeedback.html',{'feedback':feedback})
    else:
        return redirect('Guest:Login') 
    
def viewartwok(request):
    if 'adid' in request.session:
        artwork = tbl_artwork.objects.all
        return render(request, 'Admin/ViewArtwork.html',{"artwork":artwork})
    else:
        return redirect('Guest:Login')
    
def delartwork(request,id):
    tbl_artwork.objects.get(id=id).delete()
    return  redirect('Admin:viewartwok')

def complaint(request):
    if 'adid' in request.session:
        user=tbl_user.objects.all()
        artist=tbl_artist.objects.all()
        delivery=tbl_deliveryboy.objects.all()
        usercomplaint=tbl_complaint.objects.filter(user__in=user,complaint_status=0)
        artistcomplaint=tbl_complaint.objects.filter(artist__in=artist,complaint_status=0)
        deliverycomplaint=tbl_complaint.objects.filter(delivery__in=delivery,complaint_status=0)
        return render(request, 'Admin/Viewcomplaint.html',{"usercomplaint":usercomplaint,'artistcomplaint':artistcomplaint,'deliverycomplaint':deliverycomplaint})
    else:
        return redirect('Guest:Login') 
    

def reply(request,id):
    if 'adid' in request.session:
        reply=tbl_complaint.objects.get(id=id)
        if request.method=="POST":
            reply.complaint_replay=request.POST.get("txtreply")
            reply.complaint_status=1
            reply.save()
            return redirect("Admin:complaint" )
        else:
            return render(request,'Admin/Reply.html',{"reply":reply})
    else:
        return redirect('Guest:Login') 
        
 
def replayedcomplaint(request):
    if 'adid' in request.session:
        user=tbl_user.objects.all()
        artist=tbl_artist.objects.all()
        delivery=tbl_deliveryboy.objects.all()
        replayedusercomplaint=tbl_complaint.objects.filter(user__in=user,complaint_status=1)
        replayedartistcomplaint=tbl_complaint.objects.filter(artist__in=artist,complaint_status=1)
        replayeddeliverycomplaint=tbl_complaint.objects.filter(delivery__in=delivery,complaint_status=1)
        return render(request,'Admin/ReplyedComplaints.html',{"replayedusercomplaint":replayedusercomplaint,'replayeddeliverycomplaint':replayeddeliverycomplaint,"replayedartistcomplaint":replayedartistcomplaint})
    else:
        return redirect('Guest:Login') 

def viewticketbooking(request, id):
    book = tbl_ticket_booking.objects.filter(event=id)
    event = tbl_event.objects.get(id=id)
    bookcount = tbl_tickets.objects.filter(booking__event=id,booking__booking_status=1,status=0).count()
    remain = int(event.event_count) - int(bookcount)
    return render(request,"Admin/ViewEvent_Booking.html",{"data":book,"booking":bookcount,"remain":remain})

def adminprofile(request):
    if 'adid' in request.session:
         admin=tbl_Adminreg.objects.get(id=request.session['adid'])
         return render(request, 'Admin/AdminProfile.html',{'admin':admin})
    else:
        return redirect('Guest:Login') 
    
def dverification(request):
    delivery=tbl_deliveryboy.objects.all
    return render(request, 'Admin/Deliveryboy.html',{'delivery':delivery})

def deliveryaccept(request,id):
    delivery = tbl_deliveryboy.objects.get(id=id)
    delivery.deliveryboy_status = 1
    delivery.save()
    return redirect("Admin:dverification")

def deliveryreject(request,id):
    delivery = tbl_deliveryboy.objects.get(id=id)
    delivery.deliveryboy_status = 2
    delivery.save()
    return redirect("Admin:dverification")



