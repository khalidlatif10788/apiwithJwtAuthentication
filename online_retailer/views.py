

from .models import product,order,customer
from .Serializers import productSerializer,orderSerializer,customerSerializer,userRegisterSerializer,userLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Api code

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class userRegisterApiView(APIView):

    def post(self, request, format=None):
        
        serilizer= userRegisterSerializer(data=request.data)
        if serilizer.is_valid(raise_exception=True):
         user = serilizer.save()
         token =get_tokens_for_user(user)
         return Response({"token":token,"msg":"you are registered sucessfully"})
        else:
         return Response(serilizer.errors)
    

class userLoginApiView(APIView):

    def post(self, request, format=None):
        
        serilizer= userLoginSerializer(data=request.data)
        if serilizer.is_valid(raise_exception=True):
         uname=serilizer.data.get("username")
         password=serilizer.data.get("password")
         user= authenticate(username=uname,password=password)
         if user != None:
            token = get_tokens_for_user(user)
            return Response({"token":token,"msg":"you are login sucessfully"})
         else:
          return Response({"msg":"you are enter wrong username or password"})
        else:
          return Response(serilizer.errors)
 
class productApiView(APIView):

    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None,format= None):
        if request.method == 'GET':
         id = pk
         if id is not None:
          stu = product.objects.get(id=id)
          serilizer = productSerializer(stu)
          return Response(serilizer.data)
         else:
          stu = product.objects.all()
          serilizer = productSerializer(stu, many=True)
          return Response(serilizer.data)

    def post(self, request, format=None):
        serilizer= productSerializer(data=request.data)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has added sucessfully"})
        else:
         return Response(serilizer.errors)
    
    def put(self, request,pk= None, format=None):
        id = pk
        stu= product.objects.get(id=id)
        serilizer= productSerializer(stu, data=request.data, partial=True)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has updated sucessfully"})
        else:
         return Response(serilizer.errors)
 
 
    def delete(self, request,pk= None, format=None):
        id = pk
        stu= product.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"data deleted"}) 
    
# order class

class orderApiView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None,format= None):
        if request.method == 'GET':
         id = pk
         if id is not None:
          stu = order.objects.get(id=id)
          serilizer = orderSerializer(stu)
          return Response(serilizer.data)
         else:
          stu = order.objects.all()
          serilizer = orderSerializer(stu, many=True)
          return Response(serilizer.data)

    def post(self, request, format=None):
        serilizer= orderSerializer(data=request.data)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has added sucessfully"})
        else:
         return Response(serilizer.errors)
    
    def put(self, request,pk= None, format=None):
        id = pk
        stu= order.objects.get(id=id)
        serilizer= orderSerializer(stu, data=request.data, partial=True)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has updated sucessfully"})
        else:
         return Response(serilizer.errors)
 
 
    def delete(self, request,pk= None, format=None):
        id = pk
        stu= order.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"data deleted"}) 
    
    #Customer class
    
class customerApiView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,pk=None,format= None):
        if request.method == 'GET':
         id = pk
         if id is not None:
          stu = customer.objects.get(id=id)
          serilizer = customerSerializer(stu)
          return Response(serilizer.data)
         else:
          stu = customer.objects.all()
          serilizer = customerSerializer(stu, many=True)
          return Response(serilizer.data)

    def post(self, request, format=None):
        serilizer= customerSerializer(data=request.data)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has added sucessfully"})
        else:
         return Response(serilizer.errors)
    
    def put(self, request,pk= None, format=None):
        id = pk
        stu= customer.objects.get(id=id)
        serilizer= customerSerializer(stu, data=request.data, partial=True)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has updated sucessfully"})
        else:
         return Response(serilizer.errors)
 
 
    def delete(self, request,pk= None, format=None):
        id = pk
        stu= customer.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"data deleted"}) 