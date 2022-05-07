from django.http import HttpResponseRedirect
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView
from users.forms import CustomSignupForm, CustomLoginForm


# Create your views here.


class loginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomLoginForm


class signupView(SignupView):
    template_name = 'account/register.html'
    form_class = CustomSignupForm


def index(request):
    return render(request, 'home/index.html', {"": ""})