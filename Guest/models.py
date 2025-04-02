from django.db import models
from Admin.models import *

# Create your models here.

class tbl_user(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30)
    user_contact = models.CharField(max_length=30)
    user_address = models.CharField(max_length=50)
    user_password = models.CharField(max_length=30)
    user_photo = models.FileField(upload_to='Assets/User/Photo/')
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)
    
class tbl_artist(models.Model):
        artist_name = models.CharField(max_length=30)
        artist_email = models.CharField(max_length=30)
        artist_contact = models.CharField(max_length=30)
        artist_address = models.CharField(max_length=50)
        artist_photo = models.FileField(upload_to='Assets/User/Photo/')
        artist_proof = models.FileField(upload_to='Assets/User/Photo/')
        artist_password = models.CharField(max_length=30)
        place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
        artist_status=models.IntegerField(default=0)

class tbl_deliveryboy(models.Model):
        deliveryboy_name = models.CharField(max_length=30)
        deliveryboy_email = models.CharField(max_length=30)
        deliveryboy_contact = models.CharField(max_length=30)
        deliveryboy_address = models.CharField(max_length=50)
        deliveryboy_photo = models.FileField(upload_to='Assets/User/Photo/')
        deliveryboy_proof = models.FileField(upload_to='Assets/User/Photo/')
        deliveryboy_password = models.CharField(max_length=30)
        place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
        deliveryboy_status=models.IntegerField(default=0)





