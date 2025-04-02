from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# Create your views here.

def logout(request):
      del request.session["did"]
      return redirect('Guest:index')

def dhomepage(request):
    if 'did' in request.session:
          return render(request, 'DeliveryBoy/HomePage.html')
    else:
        return redirect('Guest:Login')
    
def deliveryboyprofile(request):
    if 'did' in request.session:
         delivery=tbl_deliveryboy.objects.get(id=request.session['did'])
         return render(request, 'DeliveryBoy/DeliveryboyProfile.html',{'delivery':delivery})
    else:
        return redirect('Guest:Login')  

def deliveryedit(request):
    if 'did' in request.session:
         delivery=tbl_deliveryboy.objects.get(id=request.session['did'])
         if request.method == "POST":
              delivery.deliveryboy_name=request.POST.get("txtname")
              delivery.deliveryboy_email=request.POST.get("txtemail")
              delivery.deliveryboy_contact=request.POST.get("txtcontact")
              delivery.deliveryboy_address=request.POST.get("txtaddress")
              delivery.save()
              return redirect("DeliveryBoy:deliveryboyprofile")
         else:
            return render(request, 'DeliveryBoy/DeliveryEdit.html',{'delivery':delivery})
    else:
        return redirect('Guest:Login') 
    
def changedeliveryboypassword(request):
     if 'did' in request.session:
          npassword=request.POST.get('txtpass')
          rpassword=request.POST.get('txtpd')
          opassword=request.POST.get('txtpwd')
          delivery=tbl_deliveryboy.objects.get(id=request.session['did'])
          if request.method=="POST":
               if delivery.deliveryboy_password == opassword:
                    if npassword==rpassword:
                         delivery.deliveryboy_password=request.POST.get("txtpass")
                         delivery.save()
                         return redirect("DeliveryBoy:deliveryboyprofile")
                    else:
                         return render(request,'DeliveryBoy/ChangeDeliveryBoyPassword.html',{"msg":"Error in Cpnfirm password"})
               else:
                    return render(request,'DeliveryBoy/ChangeDeliveryBoyPassword.html',{"msg":"Error in Old password"})
          else:
              return render(request,'DeliveryBoy/ChangeDeliveryBoyPassword.html')
     else:
        return redirect('Guest:Login') 
     
def complaint(request):
    if 'did' in request.session:
          complaint=tbl_complaint.objects.filter(delivery=request.session['did'])
          if request.method == "POST":
            tbl_complaint.objects.create(delivery=tbl_deliveryboy.objects.get(id=request.session['did']),
                                        complaint_title=request.POST.get("txttitle"),
                                        complaint_content=request.POST.get("txtcontent"))
            return redirect("DeliveryBoy:complaint")
          else:
               return render(request, 'DeliveryBoy/Complaint.html',{'complaint':complaint})
    else:
        return redirect('Guest:Login')     


def viewbooking(request):
     delivery = tbl_deliveryboy.objects.get(id=request.session["did"])
     book = tbl_booking.objects.filter(booking_status=2,user__place=delivery.place.id)
     return render(request,"DeliveryBoy/ViewBooking.html",{'book':book})

def orderupdation(request, id, status):
    book = tbl_booking.objects.get(id=id)
    if book.deliveryboy == None:
     book.deliveryboy = tbl_deliveryboy.objects.get(id=request.session["did"])
    book.booking_status = status
    book.save()
    return redirect("DeliveryBoy:dhomepage")

def myorder(request):
     book = tbl_booking.objects.filter(booking_status__gt=2,deliveryboy=request.session["did"])
     return render(request,"DeliveryBoy/MyOrder.html",{'book':book})