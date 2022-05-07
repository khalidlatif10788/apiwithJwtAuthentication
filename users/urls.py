from django.urls import path, include
from allauth.account.views import LogoutView
from .views import signupView, loginView, index

app_name = 'users'
urlpatterns = [
    # path('', index, name=''),
    path('home' , index, name='home'),
    path('signup/' ,signupView.as_view(), name='signup'),
    path('login/' , loginView.as_view(), name='login'),
    path('logout/' , LogoutView.as_view(),name='logout'),
]