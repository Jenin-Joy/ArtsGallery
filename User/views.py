from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Artist.models import *
from User.models import *
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime, timedelta , time, datetime
# Create your views here.
def homepage(request):
    if 'uid' in request.session:
          return render(request, 'User/HomePage.html')
    else:
        return redirect('Guest:Login')
          

def logout(request):
      del request.session["uid"]
      return redirect('Guest:index')

def myprofile(request):
    if 'uid' in request.session:
          user=tbl_user.objects.get(id=request.session['uid'])
          return render(request, 'User/MyProfile.html',{'user':user})
    else:
          return redirect('Guest:Login')



def editprofile(request):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        if request.method == "POST":
                    user.user_name=request.POST.get("txtname")
                    user.user_email=request.POST.get("txtemail")
                    user.user_contact=request.POST.get("txtcontact")
                    user.user_address=request.POST.get("txtaddress")
                    user.save()
                    return redirect("User:myprofile")
        else:
                    return render(request, 'User/EditProfile.html',{'user':user})
    else:
          return redirect('Guest:Login')

def changepassword(request):
    if 'uid' in request.session:
        npassword=request.POST.get('txtpass')
        rpassword=request.POST.get('txtpd')
        opassword=request.POST.get('txtpwd')
        user=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            if user.user_password == opassword:
                if npassword==rpassword:
                    user.user_password=request.POST.get("txtpass")
                    user.save()
                    return redirect("User:myprofile")
                else:
                        return render(request,'User/ChangePassword.html',{"msg":"Error in Cpnfirm password"})
            else:
                return render(request,'User/ChangePassword.html',{"msg":"Error in Old password"})
        else:
            return render(request,'User/ChangePassword.html')
    else:
        return redirect('Guest:Login')
     
def viewartwork(request):
    if 'uid' in request.session:
        search_query= request.GET.get('search', '')
        artwork = tbl_artwork.objects.filter(artwork_status=0)
        cat=tbl_category.objects.all()

        if search_query:
            artwork=artwork.filter(artwork_name__icontains=search_query)
        if request.method == "POST":
               tbl_artwork.objects.create(artwork_photo=request.FILES.get("txtphoto"),
                artwork_price=request.POST.get("txtprice"),
                artwork_name=request.POST.get("txtname"),
                artwork_description=request.POST.get("txtdescription"),
                artist=tbl_artist.objects.get(id=request.session['aid']),
               category=tbl_category.objects.get(id=request.POST.get('sel_category')))

               return redirect("User:viewartwork")
        else:
            return render(request, 'User/ViewWork.html',{"category":cat,"artwork":artwork,"search_query":search_query})
    else:
          return redirect('Guest:Login')



def ajaxsearch(request):
    if (request.GET.get("pid")):
        artwork = tbl_artwork.objects.filter(artwork_status=0,category=request.GET.get("pid"))
        return render(request, 'User/AjaxSearch.html',{"artwork":artwork})
    else:
        return render(request, 'User/AjaxSearch.html',{"msg":"No Result Found"})
         
    
    
     
        

def artist(request,id):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    artist=tbl_artist.objects.get(id=id)
    tot=0
    ratecount=tbl_rating.objects.filter(artist=artist).count()
    if ratecount>0:
        ratedata=tbl_rating.objects.filter(artist=artist)
        for j in ratedata:
            tot=tot+j.rating_data
            avg=tot//ratecount
            # print(avg)
            
        parry.append(avg)
    else:
        parry.append(0)
    print(parry)
    return render(request,'User/ViewArtist.html',{'artist':artist,'parry':parry,'ar':ar})

def viewevent(request):
    if 'uid' in request.session:
        event = tbl_event.objects.all()
        return render(request, 'User/ViewEvent.html',{"event":event})
    else:
          return redirect('Guest:Login')
        
def bookingartwork(request,id):
      if 'uid' in request.session:
               tbl_booking.objects.create(user=tbl_user.objects.get(id=request.session['uid']),
                                          artwork=tbl_artwork.objects.get(id = id))
               return redirect("User:mybooking")
      else:
          return redirect('Guest:Login')

def mybooking(request):
    if 'uid' in request.session:
        booking=tbl_booking.objects.filter(user=request.session['uid'])
        tbook = tbl_ticket_booking.objects.filter(user=request.session["uid"])
        return render(request, 'User/MyBooking.html',{"booking":booking,"data":tbook})
    else:
          return redirect('Guest:Login')

def tickets(request,id):
    tic = tbl_tickets.objects.filter(booking=id,status=0)
    return render(request,"User/Tickets.html",{"data":tic})

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

def BookEvent(request,id):
    if 'uid' in request.session:
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
                ticket_count = tbl_ticket_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
                if ticket_count > 0:
                    bk = tbl_ticket_booking.objects.get(user=request.session["uid"],booking_status=0)
                    for s in seat:
                        tic_count = tbl_tickets.objects.filter(booking=bk.id,seat_no=s).count()
                        if tic_count > 0:
                            return render(request,"User/BookEvent.html",{"msg1":"You Already Booked Seat "+s,"id":id})
                        else:
                            tbl_tickets.objects.create(seat_no=s,booking=tbl_ticket_booking.objects.get(id=bk.id))
                    bk_amt = bk.booking_totalamount
                    tot = int(bk_amt) + total
                    bk.booking_totalamount = tot
                    bk.save()
                    return render(request,"User/BookEvent.html",{"msg":"Booked","id":bk.id})
                else:
                    bkid = tbl_ticket_booking.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),booking_totalamount=total,booking_time=datetime.now(),event=tbl_event.objects.get(id=id))
                    for s in seat:
                        tbl_tickets.objects.create(seat_no=s,booking=tbl_ticket_booking.objects.get(id=bkid.id))
                    return render(request,"User/BookEvent.html",{"msg":"Booked","id":bkid.id})
            else:
                 return render(request,"User/BookEvent.html",{"msg1":"No Seat Booked","id":id}) 
        else:
            return render(request, 'User/BookEvent.html',{"event_seat":event_seat,"gap":gap,"event":event,"book":ticketbook})
    else:
        return redirect('Guest:Login')

def ticketpayment(request,id):
    book = tbl_ticket_booking.objects.get(id=id)
    total = book.booking_totalamount
    if request.method == "POST":
        book.booking_status=1
        book.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":total})

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

def feedback(request):
    if 'uid' in request.session:
        feedback=tbl_feedback.objects.filter(user=request.session['uid'])
        if request.method == "POST":
            tbl_feedback.objects.create(user=tbl_user.objects.get(id=request.session['uid']),
                                        feedback_content=request.POST.get("txtfeedback"))
            return redirect("User:feedback")
        else:
            return render(request, 'User/Feedback.html',{'feedback':feedback})
    else:
        return redirect('Guest:Login')
      
def usercomplaint(request):
    if 'uid' in request.session:
          complaint=tbl_complaint.objects.filter(user=request.session['uid'])
          if request.method == "POST":
            tbl_complaint.objects.create(user=tbl_user.objects.get(id=request.session['uid']),
                                        complaint_title=request.POST.get("txttitle"),
                                        complaint_content=request.POST.get("txtcontent"))
            return redirect("User:usercomplaint")
          else:
               return render(request, 'User/Complaint.html',{'complaint':complaint})
    else:
        return redirect('Guest:Login')
            
def delcomplaint(request,id):
    if 'uid' in request.session:
         tbl_complaint.objects.get(id=id).delete()
         return redirect('User:usercomplaint')
    else:
        return redirect('Guest:Login')          

def payment(request, id):
    booking = tbl_booking.objects.get(id=id)
    art = tbl_artwork.objects.get(id=booking.artwork.id)
    total = art.artwork_price
    if request.method == "POST":
        booking.booking_status = 1
        booking.save()
        art.artwork_status = 1
        art.save()
        return redirect('User:loader')
    else:
        return render(request, 'User/Payment.html',{"total":total})

def loader(request):
    return render(request, 'User/Loader.html')

def paymentsuc(request):
    return render(request, 'User/Payment_suc.html')


def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(artist=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(artist=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,artist=tbl_artist.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(artist=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(artist=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(artist=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)



def chatpage(request,id):
    artist  = tbl_artist.objects.get(id=id)
    return render(request,"User/Chat.html",{"artist":artist})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_artist = tbl_artist.objects.get(id=request.POST.get("tid"))
    print(to_artist)
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,artist_to=to_artist,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(artist_from=tid) | Q(artist_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(user_to=request.GET.get("tid")) | (Q(artist_to=request.GET.get("tid")) & Q(artist_from=request.session["aid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def viewauctionlist(request):
    auction = tbl_auctionhead.objects.all()
    return render(request,"User/ViewAuctionList.html",{"auction":auction})

def auction(request, id):
    auction = tbl_auctionhead.objects.get(id=id)
    return render(request,"User/Auction.html",{"artwork":auction,"id":id})

def ajaxplacebid(request):
    if int(request.GET.get("amount")) > int(request.GET.get("amt")):
        getamount = tbl_auctionbody.objects.filter(auction=request.GET.get("auctionid")).last()
        if getamount:
            if int(getamount.auctionbody_amount) < int(request.GET.get("amount")):
                tbl_auctionbody.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),user=tbl_user.objects.get(id=request.session["uid"]),auctionbody_amount=request.GET.get("amount"))
                timer = tbl_timmer.objects.filter(auction=request.GET.get("auctionid")).count()
                if timer > 0:
                    t = tbl_timmer.objects.get(auction=request.GET.get("auctionid"))
                    t.timmer = time(0, 0, 30)  # Adds 30 seconds
                    t.save()
                else:
                    tbl_timmer.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),timmer=time(0, 0, 30))
                return JsonResponse({"msg":"Bid Placed Successfully","color":"rgb(94, 177, 97)"})
            else:
                return JsonResponse({"msg":"Please Enter Valid Amount","color":"red"})
        else:
            tbl_auctionbody.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),user=tbl_user.objects.get(id=request.session["uid"]),auctionbody_amount=request.GET.get("amount"))
            timer = tbl_timmer.objects.filter(auction=request.GET.get("auctionid")).count()
            if timer > 0:
                t = tbl_timmer.objects.get(auction=request.GET.get("auctionid"))
                t.timmer = time(0, 0, 30)  # Adds 30 seconds
                t.save()
            else:
                tbl_timmer.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),timmer=time(0, 0, 30))
            return JsonResponse({"msg":"Bid Placed Successfully","color":"rgb(94, 177, 97)"})
    else:
        return JsonResponse({"msg":"Please Enter Valid Amount","color":"red"})

def ajaxgetbid(request):
    auctionid = request.GET.get("auctionid")
    auctiondata = tbl_auctionbody.objects.filter(auction=auctionid).last()
    if auctiondata:
        return JsonResponse({"user":auctiondata.user.user_name,"amount":auctiondata.auctionbody_amount})
    else:
        return JsonResponse({"user":"","amount":0})

def ajaxclosebid(request):
    auctionid = request.GET.get("auctionid")
    auctiondata = tbl_auctionbody.objects.filter(auction=auctionid).last()
    auctionbody = tbl_auctionbody.objects.get(id=auctiondata.id)
    auctionbody.auctionbody_status = 1
    auctionbody.save()
    auctionhead = tbl_auctionhead.objects.get(id=auctiondata.auction.id)
    auctionhead.auctionhead_status = 2 
    auctionhead.auction_totalamount = auctionbody.auctionbody_amount
    auctionhead.save()
    return JsonResponse({"msg":"Auction Completed...","user":auctiondata.user.user_name,"amount":auctiondata.auctionbody_amount})

def ajaxgettimmer(request):
    auction_id = request.GET.get("auctionid")
    userdata = tbl_auctionbody.objects.filter(auction=auction_id).last()

    if userdata is not None:
        userid = userdata.user.id
        if userid == request.session["uid"]:
            timmer_count = tbl_timmer.objects.filter(auction=auction_id, timmer_status=0).count()
            if timmer_count > 0:
                t = tbl_timmer.objects.get(auction=auction_id)
                if t.timmer > time(0, 0, 0):
                    # Convert time to datetime for subtraction
                    current_time = datetime.combine(datetime.today(), t.timmer)
                    new_time = (current_time - timedelta(seconds=1)).time()

                    # Update timer in database
                    t.timmer = new_time
                    t.save()

                    return JsonResponse({"time": t.timmer, "time_up": False})
                else:   
                    # Timer expired
                    return JsonResponse({"time": time(0, 0, 0), "time_up": True})
            else:
                return JsonResponse({"time": time(0, 0, 0), "time_up": True})
        else:
            timmer_count = tbl_timmer.objects.filter(auction=auction_id).count()
            if timmer_count > 0:
                ti = tbl_timmer.objects.filter(auction=auction_id).last()
                if ti.timmer > time(0, 0, 0):
                    return JsonResponse({"time": ti.timmer, "time_up": False})
                else:
                    return JsonResponse({"time": time(0, 0, 0), "time_up": True})
            else:
                return JsonResponse({"time": time(0, 0, 0), "time_up": True})
    else:
        return JsonResponse({"time": time(0, 0, 30), "time_up": False})

def myauction(request):
    auction = tbl_auctionbody.objects.filter(user=request.session["uid"],auctionbody_status=1)
    return render(request,"User/MyAuction.html",{'auction':auction})

def auctionpayment(request, id):
    auction = tbl_auctionbody.objects.get(id=id)
    amount = auction.auctionbody_amount
    auc = tbl_auctionhead.objects.get(id=auction.auction.id)
    if request.method == "POST":
        artwork = tbl_artwork.objects.get(id=auc.artwork.id)
        artwork.artwork_status=3
        artwork.save()
        auc.auctionhead_status = 3
        auc.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":amount})