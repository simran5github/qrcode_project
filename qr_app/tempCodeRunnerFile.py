from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth import authenticate
from qr_app.models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from qrcode import *

from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')