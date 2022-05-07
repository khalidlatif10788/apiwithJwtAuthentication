from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import customer, product,order
from django.contrib.auth.models import User 

class productSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        return product.objects.create(**validate_data)

    def update(self, instance,validate_data):
     instance.P_brand= validate_data.get('P_brand', instance.P_brand)
     instance.pcate= validate_data.get('pcate', instance.pcate)
     instance.pname= validate_data.get('pname', instance.pname)
     instance.pdescription= validate_data.get('pdescription', instance.pdescription)
     instance.psalep= validate_data.get('psalep', instance.psalep)
     instance.pdiscountp= validate_data.get('pdiscountp', instance.pdiscountp)
     instance.psize= validate_data.get('psize', instance.psize)
     instance. product_stock= validate_data.get(' product_stock', instance.product_stock)
     instance.product_creation_date= validate_data.get('product_creation_date', instance.product_creation_date)
     instance.photo= validate_data.get('photo', instance.photo)
     instance.save()
     return instance
    class Meta:
        model= product
        fields=['id','P_brand','pcate','pname','pdescription','psalep','pdiscountp','psize',
                'product_stock','product_creation_date','photo']
        # fields= '__all__'
       
class orderSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        return order.objects.create(**validate_data)
    
    def update(self, instance,validate_data):
     instance.customerid= validate_data.get('customerid', instance.customerid)
     instance.amount= validate_data.get('amount', instance.amount)
     instance.order_address= validate_data.get('order_address', instance.order_address)
     instance.shipping_address= validate_data.get('shipping_address', instance.shipping_address)
     instance.order_email= validate_data.get('order_email', instance.order_email)
     instance.orderdate= validate_data.get('orderdate', instance.orderdate)
     instance.order_status= validate_data.get('order_status', instance.order_status)
     instance.save()
     return instance
    class Meta:
        model= order
        fields=['id','customerid','amount','order_address','shipping_address','order_email','orderdate','order_status']
                
        # fields= '__all__'
    
		
	
class customerSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        return order.objects.create(**validate_data)

    def update(self, instance,validate_data):
     instance.customer= validate_data.get('customer', instance.customer)
     instance.name= validate_data.get('name', instance.name)
     instance.phone= validate_data.get('phone', instance.phone)
     instance.billing_address= validate_data.get('billing_address', instance.billing_address)
     instance.shipping_address= validate_data.get('shipping_address', instance.shipping_address)
     instance.country= validate_data.get(' country', instance.country)
     
     instance.save()
     return instance
    class Meta:
        model= customer
        fields=['id','customer','name','phone','billing_address','shipping_address','country']
                
        # fields= '__all__'
     
class userRegisterSerializer(serializers.ModelSerializer):

    password2= serializers.CharField(style={'input_type':'password',})
    class Meta:
        model= User
        fields=['username','password','password2','email']
    def validate(self, attrs):
        pass1=attrs.get('password')
        pass2=attrs.get('password2')
        if str(pass1) != str(pass2):
            raise serializers.ValidationError("password not matched")
        else:
         return attrs
    def create(self, validated_data):
         validated_data.pop('password2', None)
         return User.objects.create_user(**validated_data)  
class userLoginSerializer(serializers.ModelSerializer):
    username= serializers.CharField(max_length=200)
    class Meta:
        model=User
        fields=['username','password'] 
		
	