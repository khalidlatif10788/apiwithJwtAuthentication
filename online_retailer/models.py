

# Create your models here.

from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class pcategory(models.Model):
    c_name= models.CharField(max_length=50)
    c_description= models.TextField(max_length=500)
    thumbnail= models.ImageField(upload_to='uploads/',default='Category_default.jpg')
    def __str__(self):
        return self.c_name

class brand(models.Model):
    b_name= models.CharField(max_length=50)
    b_description= models.TextField(max_length=500)
    thumbnail= models.ImageField(upload_to='uploads/',default='brand_default.jpg')
    def __str__(self):
        return self.b_name

class product(models.Model):
    P_brand= models.ForeignKey(brand, on_delete=models.CASCADE,default='1')
    pcate= models.ForeignKey(pcategory, on_delete=models.CASCADE,default='1')
    pname =models.CharField(max_length=50,verbose_name="Product")
    pdescription =models.TextField(max_length=500,verbose_name="Description")
    psalep=models.IntegerField(verbose_name="Selling Price")
    pdiscountp= models.IntegerField()
    psize=models.CharField(max_length=50,verbose_name="Size")
    product_stock= models.IntegerField()
    product_creation_date= models.DateField()
    photo=models.ImageField(upload_to='uploads/',default='default.jpg')



class customer(models.Model):

    customer= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=25,default="admin")
    phone= models.CharField(max_length=25)
    billing_address= models.TextField(max_length=400,null=True)
    shipping_address= models.TextField(max_length=400,null=True)
    country= CountryField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class cart(models.Model):
    customer= models.ForeignKey(customer, on_delete=models.CASCADE)
    prd= models.ForeignKey(product, on_delete=models.CASCADE)
    qty= models.IntegerField(default=1)
    totalAmount=models.DecimalField(max_digits=19, decimal_places=10)


class order(models.Model):

    order_CHOICES =(
    ("Pending","pending"),
    ("processing","processing"),
    ("packed","packed"),
    ("deliver","deliver"),
    ("done","done"),
      )
   
    customerid= models.ForeignKey(customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    order_address= models.TextField(max_length=400)
    shipping_address= models.TextField(max_length=400)
    order_email=models.EmailField()
    orderdate=models.DateTimeField()
    order_status= models.CharField( max_length=50,choices=order_CHOICES )


class order_detail(models.Model):
    order_id= models.ForeignKey(order, on_delete=models.CASCADE)
    product_id= models.ForeignKey(product, on_delete=models.CASCADE)
    qty= models.IntegerField(default=1)
    price = models.DecimalField(max_digits=19, decimal_places=10)



 
    


    





