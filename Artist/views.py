from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Artist.models import *
from User.models import *
from datetime import datetime
from django.db.models import Q,Max
from django.http import JsonResponse


# Create your views here.

        

def artisthomepage(request):
    if 'aid' in request.session:
         return render(request, 'Artist/ArtistHomePage.html')
    else:
        return redirect('Guest:Login')  

def logout(request):
      del request.session["aid"]
      return redirect('Guest:index')

def artistabout(request):
       return render(request,"Artist/ArtistAbout.html")

def artistprofile(request):
    if 'aid' in request.session:
         artist=tbl_artist.objects.get(id=request.session['aid'])
         return render(request, 'Artist/ArtistProfile.html',{'artist':artist})
    else:
        return redirect('Guest:Login')  

def artistedit(request):
    if 'aid' in request.session:
         artist=tbl_artist.objects.get(id=request.session['aid'])
         if request.method == "POST":
              artist.artist_name=request.POST.get("txtname")
              artist.artist_email=request.POST.get("txtemail")
              artist.artist_contact=request.POST.get("txtcontact")
              artist.artist_address=request.POST.get("txtaddress")
              artist.save()
              return redirect("Artist:artistprofile")
         else:
            return render(request, 'Artist/ArtistEdit.html',{'artist':artist})
    else:
        return redirect('Guest:Login') 
    
def changeartistpassword(request):
     if 'aid' in request.session:
          npassword=request.POST.get('txtpass')
          rpassword=request.POST.get('txtpd')
          opassword=request.POST.get('txtpwd')
          artist=tbl_artist.objects.get(id=request.session['aid'])
          if request.method=="POST":
               if artist.artist_password == opassword:
                    if npassword==rpassword:
                         artist.artist_password=request.POST.get("txtpass")
                         artist.save()
                         return redirect("Artist:artistprofile")
                    else:
                         return render(request,'Artist/ChangeArtistPassword.html',{"msg":"Error in Cpnfirm password"})
               else:
                    return render(request,'Artist/ChangeArtistPassword.html',{"msg":"Error in Old password"})
          else:
              return render(request,'Artist/ChangeArtistPassword.html')
     else:
        return redirect('Guest:Login') 
     
def addartwork(request):
    if 'aid' in request.session:
        artwork = tbl_artwork.objects.filter(artist=request.session['aid'])
        # artwork = tbl_artwork.objects.filter(artwork_status=0)
        cat=tbl_category.objects.all()
        if request.method == "POST":
               tbl_artwork.objects.create(artwork_photo=request.FILES.get("txtphoto"),
                artwork_name=request.POST.get("txtname"),
                artwork_price=request.POST.get("txtprice"),
                artwork_description=request.POST.get("txtdescription"),
                artist=tbl_artist.objects.get(id=request.session['aid']),
                category=tbl_category.objects.get(id=request.POST.get('sel_category')))
               

               return redirect("Artist:addartwork")
        else:
               return render(request, 'Artist/AddArtwork.html',{"category":cat,"artwork":artwork})
    else:
        return redirect('Guest:Login') 
     
def delartwork(request,id):
    tbl_artwork.objects.get(id=id).delete()
    return redirect('Artist:addartwork')

def viewbooking(request):
    if 'aid' in request.session:
         viewbooking=tbl_booking.objects.all()
         user=tbl_user.objects.all()
         tbook = tbl_ticket_booking.objects.filter(artist=request.session["aid"])
         return render(request, 'Artist/ViewBooking.html',{'viewbooking':viewbooking,'user':user,"data":tbook})
    else:
        return redirect('Guest:Login') 

def artistcomplaint(request):
    if 'aid' in request.session:
         complaint=tbl_complaint.objects.filter(artist=request.session['aid'])
         if request.method == "POST":
            tbl_complaint.objects.create(complaint_title=request.POST.get("txttitle"),
                                        complaint_content=request.POST.get("txtcontent"),
                                        artist=tbl_artist.objects.get(id=request.session['aid']))
            return redirect("Artist:artistcomplaint")
         else:
            return render(request, 'Artist/ArtistComplaint.html',{'complaint':complaint})
    else:
        return redirect('Guest:Login') 

def delcomplaint(request,id):
    if 'aid' in request.session:
        tbl_complaint.objects.get(id=id).delete()
        return redirect('Artist:artistcomplaint')   
    else:
        return redirect('Guest:Login')        
    


def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Artist/Chat.html",{"user":user})

def ajaxchat(request):
    from_artist = tbl_artist.objects.get(id=request.session["aid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),artist_from=from_artist,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Artist/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    artist = tbl_artist.objects.get(id=request.session["aid"])
    chat_data = tbl_chat.objects.filter((Q(artist_from=artist) | Q(artist_to=artist)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Artist/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(artist_from=request.session["aid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(artist_to=request.session["aid"]))).delete()
    return render(request,"Artist/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def chatlist(request):
    chat = tbl_chat.objects.filter(artist_to=request.session['aid']).order_by('-chat_time')
    print(chat)
    return render(request,'Artist/ChatList.html',{'chat':chat})

from django.utils import timezone

def viewevent(request):
    if 'aid' in request.session:
        current_date = timezone.now().date()
        events = tbl_event.objects.all()
        upcoming_events = events.filter(event_todate__gte=current_date)
        finished_events = events.filter(event_todate__lt=current_date)
        return render(request, 'Artist/ViewEvent.html', {
            "upcoming_events": upcoming_events,
            "finished_events": finished_events
        })
    else:
        return redirect('Guest:Login')
    
def BookEvent(request,id):
    if 'aid' in request.session:
        event = tbl_event.objects.get(id=id)
        event_seat = range(1,int(event.event_count)+1)
        # print(event_seat)
        gap = []
        j = 1
        for i in event_seat:
            if i/10 == j:
                gap.append(i)
                j=j+1
        ticketbook = tbl_tickets.objects.filter(Q(booking__booking_status=1,status=0,booking__event=id) | Q(booking__booking_status=0,status=0,booking__event=id))
        if request.method == "POST":
            seat_count = len(request.POST.getlist("txtseat[]"))
            if seat_count > 0:
                seat = request.POST.getlist("txtseat[]")
                event_amt = event.event_price
                total = int(event_amt) * seat_count
                ticket_count = tbl_ticket_booking.objects.filter(artist=request.session["aid"],booking_status=0).count()
                if ticket_count > 0:
                    bk = tbl_ticket_booking.objects.get(artist=request.session["aid"],booking_status=0)
                    for s in seat:
                        tic_count = tbl_tickets.objects.filter(booking=bk.id,seat_no=s).count()
                        if tic_count > 0:
                            return render(request,"Artist/BookEvent.html",{"msg1":"You Already Booked Seat "+s,"id":id})
                        else:
                            tbl_tickets.objects.create(seat_no=s,booking=tbl_ticket_booking.objects.get(id=bk.id))
                    bk_amt = bk.booking_totalamount
                    tot = int(bk_amt) + total
                    bk.booking_totalamount = tot
                    bk.save()
                    return render(request,"Artist/BookEvent.html",{"msg":"Booked","id":bk.id})
                else:
                    bkid = tbl_ticket_booking.objects.create(artist=tbl_artist.objects.get(id=request.session["aid"]),booking_totalamount=total,booking_time=datetime.now(),event=tbl_event.objects.get(id=id))
                    for s in seat:
                        tbl_tickets.objects.create(seat_no=s,booking=tbl_ticket_booking.objects.get(id=bkid.id))
                    return render(request,"Artist/BookEvent.html",{"msg":"Booked","id":bkid.id})
            else:
                 return render(request,"Artist/BookEvent.html",{"msg1":"No Seat Booked","id":id}) 
        else:
            return render(request, 'Artist/BookEvent.html',{"event_seat":event_seat,"gap":gap,"event":event,"book":ticketbook})
    else:
        return redirect('Guest:Login')
    
def ticketpayment(request,id):
    book = tbl_ticket_booking.objects.get(id=id)
    total = book.booking_totalamount
    if request.method == "POST":
        book.booking_status=1
        book.save()
        return redirect("Artist:loader")
    else:
        return render(request,"Artist/Payment.html",{"total":total})
    
def loader(request):
    return render(request, 'Artist/Loader.html')

def paymentsuc(request):
    return render(request, 'Artist/Payment_suc.html')

def bookchecking(request):
   # print("hai")
    min = request.GET.get("min")
    hournow = request.GET.get("hour")
    # print(min)
    tbook = tbl_ticket_booking.objects.filter(booking_status=0)
    for  t in tbook:
        time = t.booking_time.minute
        hour = t.booking_time.hour
        # print(hour)
        if int(hournow) > hour:
            diff = (60 + int(min)) - time
        else:
            diff = int(min) - time
        # print(diff)
        if diff > 5:
            tickets = tbl_tickets.objects.filter(booking=t.id)
            for ti in tickets:
                tbl_tickets.objects.get(id=ti.id).delete()
            tbl_ticket_booking.objects.get(id=t.id).delete()
    # print(datetime.now().minute)
    return JsonResponse({"msg":"hai Hello"})

def tickets(request,id):
    tic = tbl_tickets.objects.filter(booking=id,status=0)
    return render(request,"Artist/Tickets.html",{"data":tic})

def cancelbooking(request):
    bk = tbl_tickets.objects.get(id=request.GET.get("tid"))
    ticket = tbl_tickets.objects.filter(booking=bk.booking.id,status=0).count()
    if ticket > 1:
        bk.status = 1
        bk.save()
        return JsonResponse({"msg":"Ticket Cancelled.."})
    else:
        bk.status=1
        bk.save()
        book = tbl_ticket_booking.objects.get(id=bk.booking.id)
        book.booking_status=2
        book.save()
        return JsonResponse({"msg1":"Ticket Cancelled.."})

def orderupdation(request, id, status):
    book = tbl_booking.objects.get(id=id)
    book.booking_status = status
    book.save()
    return redirect("Artist:viewbooking")

def addtoauction(request,id):
   artwork = tbl_artwork.objects.get(id=id) 
   if request.method == "POST":
    auctioncount = tbl_auctionhead.objects.filter(artwork=artwork).count()
    if auctioncount > 0:
        return render(request,"Artist/AddToAuction.html",{"msg":"This Product Already Added To Auction Thank You..!!","id":id})
    else:
        tbl_auctionhead.objects.create(artwork=artwork,
                                        auctionhead_amount=request.POST.get('txt_amount'),
                                        auctionhead_todate=request.POST.get('txt_todate'),
                                        auction_starttime=request.POST.get('txt_starttime'))
        artwork.artwork_status = 2
        artwork.save()
        return render(request,"Artist/AddToAuction.html",{"msg":"Product Added To Auction List","id":id})
   return render(request,"Artist/AddToAuction.html",{"data":artwork})

def auctionlist(request):
    auction = tbl_auctionhead.objects.filter(artwork__artist=request.session["aid"],auctionhead_status__lt=3)
    return render(request,"Artist/AuctionList.html",{"auction":auction})

def auctionupdation(request, id, status):
    auction = tbl_auctionhead.objects.get(id=id)
    auction.auctionhead_status = status
    auction.save()
    return redirect('Artist:auctionlist')

def completedauction(request):
    auction = tbl_auctionhead.objects.filter(
        artwork__artist=request.session["aid"],
        auctionhead_status__gt=2
    ).select_related(
        'deliveryboy',  # Include delivery boy details
        'artwork__artist'
    )
    for i in auction:
        aucbody = tbl_auctionbody.objects.get(auction=i.id, auctionbody_status=1)
        i.user = aucbody.user.user_name
    return render(request, "Artist/CompletedAuction.html", {"auction": auction})

# Removed assign_deliveryboy and assign_deliveryboy_action functions
