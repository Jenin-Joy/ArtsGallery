from django.db import models
from Admin.models import *
from Guest.models import *
from Artist.models import *

# Create your models here.
class tbl_booking(models.Model):
        booking_date=models.DateField(auto_now_add=True)
        booking_status = models.IntegerField(default=0)
        user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
        artwork = models.ForeignKey(tbl_artwork, on_delete=models.CASCADE)
        deliveryboy = models.ForeignKey(tbl_deliveryboy, on_delete=models.CASCADE, null=True)


class tbl_ticket_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE, null=True)
    artist=models.ForeignKey(tbl_artist,on_delete=models.CASCADE, null=True)
    booking_status=models.IntegerField(default=0)
    booking_totalamount=models.CharField(max_length=50,null=True)
    booking_time = models.TimeField()
    event = models.ForeignKey(tbl_event,on_delete=models.CASCADE)

class tbl_tickets(models.Model):
    booking = models.ForeignKey(tbl_ticket_booking,on_delete=models.CASCADE)
    seat_no = models.IntegerField()
    status = models.IntegerField(default=0)

class tbl_feedback(models.Model):
        feedback_content =models.CharField(max_length=50)
        feedback_date=models.DateField(auto_now_add=True)
        user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_complaint(models.Model):
   complaint_title = models.CharField(max_length=30)
   complaint_content= models.CharField(max_length=30)
   complaint_date = models.DateField(auto_now_add=True)
   complaint_status = models.IntegerField(default=0)
   complaint_replay = models.CharField(max_length=30)
   user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
   artist = models.ForeignKey(tbl_artist, on_delete=models.CASCADE,null=True)
   delivery = models.ForeignKey(tbl_deliveryboy, on_delete=models.CASCADE,null=True)


class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    artist=models.ForeignKey(tbl_artist,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)


class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    artist_to = models.ForeignKey(tbl_artist,on_delete=models.CASCADE,related_name="artist_to",null=True)
    artist_from = models.ForeignKey(tbl_artist,on_delete=models.CASCADE,related_name="artist_from",null=True)

class tbl_auctionbody(models.Model):
    auctionbody_amount = models.CharField(max_length=30)
    auction = models.ForeignKey(tbl_auctionhead, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    auctionbody_status = models.IntegerField(default=0)

class tbl_timmer(models.Model):
    timmer = models.TimeField()
    auction = models.ForeignKey(tbl_auctionhead, on_delete=models.CASCADE)
    timmer_status = models.IntegerField(default=0)