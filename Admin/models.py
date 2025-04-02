from django.db import models



# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_Adminreg(models.Model):
    Adminreg_name=models.CharField(max_length=50)
    Adminreg_Email=models.CharField(max_length=50)
    Adminreg_password=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    Subcategory_name=models.CharField(max_length=50)
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)



class tbl_product(models.Model):
        product_name=models.CharField(max_length=50)
        product_price=models.CharField(max_length=50)
        product_details=models.CharField(max_length=500)
        subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
        product_photo=models.FileField(upload_to='Assets/User/Photo/')


class tbl_event(models.Model):
        event_name=models.CharField(max_length=50)
        event_description=models.CharField(max_length=50)
        event_count=models.CharField(max_length=50)
        event_todate = models.CharField(max_length=50)
        event_status = models.IntegerField(default=0)
        event_price = models.CharField(max_length=50)


