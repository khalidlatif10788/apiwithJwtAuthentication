
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from online_retailer import views


urlpatterns = [
    # api product retrive url
    path('productReterive/',views.productApiView.as_view(), name="product" ),
    path('productReterive/<int:pk>',views.productApiView.as_view()),
    
    # order url
    path('orderReterive/',views.orderApiView.as_view(), name="order" ),
    path('orderReterive/<int:pk>',views.orderApiView.as_view()),
    #customr url
    path('customerReterive/',views.customerApiView.as_view(), name="customer" ),
    path('customerReterive/<int:pk>',views.customerApiView.as_view()),
  
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
