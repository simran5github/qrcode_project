from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth import authenticate
from qr_app.models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from qrcode import *
from django.contrib import messages
import random
from random import randint
from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def do(request):
    return render(request,'do.html')
def genqr(request):
    return render(request,'genqr.html')
def portfolio(request):
    oks=qr_model_auth.objects.filter(user=request.user)

    ss=User.objects.get(username=request.user)
    return render(request,'portfolio.html',{'myname':ss,'oks':oks})

def privacy(request):
    return render(request,'privacy.html')
def signin(request):
    return render(request,'signin.html')
def signup(request):
    if request.method=="POST":
        user_name=request.POST['name']
        user_password=request.POST['password']
        user_email=request.POST['email']
        request.session['name']=user_name
        request.session['email']=user_email
        request.session['password']=user_password
        user_cpassword=request.POST['cpassword']
        if user_password==user_cpassword:
            if User.objects.filter(email=user_email):
             messages.error(request,'User Already Exists')
             return redirect('signup')
            else:

                
                User.objects.create_user(username=user_name,password=user_password,email=user_email)

                send_mail(
                    # "Luna Work's",
                    # f"hi {user_name} thanks for signup with Luna Work",
                    "Welcome to SparkQR - Igniting Your QR Code Experience!",
                    f"Dear {user_name}, \nGreetings from SparkQR! We're excited to welcome you to our vibrant community of QR code enthusiasts. Your registration has been successfully authenticated, and you are now ready to spark creativity with QR codes on our platform.\nHave questions, suggestions, or just want to share your SparkQR experience? Our support team is ready to assist. Feel free to reach out through our Contact Us section for prompt and friendly assistance.\n\nThank you for choosing SparkQR. Let the sparks fly as you embark on a QR code journey filled with creativity and innovation.\nSpark on!\nBest Regards\nThe SparkQR Team",
                    "lunawork04@gmail.com",
                    [user_email],
                    fail_silently=False,
                )

                return redirect('signin')
        else:
            messages.error(request,'Passwords do not Match. Please try again!')
            return redirect('signup')

    else:
        return render(request,'signup.html')
    

def signin(request):
    if request.method=="POST":
        user_signname=request.POST['username']
        password=request.POST['password']
        my_user=auth.authenticate(username=user_signname,password=password)
        if my_user is not None:
            auth.login(request,my_user)
            return render(request,'regindex.html',{'myname':user_signname})
        else:
            messages.error(request,'Invalid User')
            return redirect('signin')
    else:
        return render(request,'signin.html')

def loogout(request):
    auth.logout(request)
    return redirect('index')

def termsofuse(request):
    return render(request,'termsofuse.html')

def Take_Review(request):
    if request.method=='POST':
        R_name=request.POST['Rname']
        R_mobile=request.POST['Rmobile']
        R_email=request.POST['Remail']
        R_profile=request.POST['Rprofile']
        R_msg=request.POST['Rmsg']
        R_review=request.POST['Rreview']
        R_country=request.POST['Rcountry']
        Review.objects.create(reviewer_name=R_name,reviewer_mobile=R_mobile,reviewer_email=R_email,reviewer_profile=R_profile,reviewer_message=R_msg,reviewer_review=R_review,reviewer_country=R_country)
        return redirect('contact')
    else:
        return render(request,'contact.html')
    
def reg_Take_Review(request):
    if request.method=='POST':
        R_name=request.POST['Rname']
        R_mobile=request.POST['Rmobile']
        R_email=request.POST['Remail']
        R_profile=request.POST['Rprofile']
        R_msg=request.POST['Rmsg']
        R_review=request.POST['Rreview']
        R_country=request.POST['Rcountry']
        Review.objects.create(reviewer_name=R_name,reviewer_mobile=R_mobile,reviewer_email=R_email,reviewer_profile=R_profile,reviewer_message=R_msg,reviewer_review=R_review,reviewer_country=R_country)
        return redirect('regcontact')
    else:
        return render(request,'regcontact.html')


def search_qro(request):
    if request.method=='POST':
        o=request.POST['vikas']
        qr_model(name=o).save()
        qrc=qr_model.objects.all().last()
        return render(request,'genqr.html',{'qrc':qrc})
    else:
       return render(request,'genqr.html')
    

# def user_his(request):
#     if request.method=='POST':
#         s=qr_user_history.User.objects.get(username=request.user)
#         o=request.POST['vikas']
#         s.qr_model(name=o).save()

#         qrc=qr_model.objects.all().last()
#         return render(request,'genqr.html',{'qrc':qrc})
#     else:
#        return render(request,'genqr.html')


        




# simple QR code
# immg=qrcode.make('https://www.youtube.com')
# immg.save('ok.jpg') 
# immg.show('ok.jpg')

# advanced QR code
# c='https://www.instagram.com/iarrav/'
# a=qrcode.QRCode(version=2, box_size=5,border=2)
# a.add_data(c)
# a.make(fit=True)
# img=a.make_image(fill_color='pink',back_color='white')
# img.save('okl.jpg') 
# img.show('okl.jpg')

#registered users#
def regindex(request):
    ss=User.objects.get(username=request.user)
    return render(request,'regindex.html',{'myname':ss})
def regabout(request):
    ss=User.objects.get(username=request.user)
    return render(request,'regabout.html',{'myname':ss})
def regcontact(request):
    ss=User.objects.get(username=request.user)
    return render(request,'regcontact.html',{'myname':ss})
def regdo(request):
    ss=User.objects.get(username=request.user)
    return render(request,'regdo.html',{'myname':ss})
def reggenqr(request):
    ss=User.objects.get(username=request.user)
    return render(request,'reggenqr.html',{'myname':ss})
def regprivacy(request):
    ss=User.objects.get(username=request.user)
    return render(request,'regprivacy.html',{'myname':ss})
def regtermsofuse(request):
    ss=User.objects.get(username=request.user)
    return render(request,'regtermsofuse.html',{'myname':ss})
##

def home(request):
    if request.method == 'POST':
        name = request.POST['vikas']
        if request.user.is_authenticated:
            user = request.user
            qr_model_auth(name=name, user=user).save()
            data = qr_model_auth.objects.all().last
            ss=User.objects.get(username=request.user)
            return render(request, 'reggenqr.html',{'data':data,'myname':ss})
        else:
            qr_model(name=name).save()
            data = qr_model.objects.all().last()
            ss=User.objects.get(username=request.user)
            return render(request, 'reggenqr.html',{'data':data,'myname':ss})
    else:
        ss=User.objects.get(username=request.user)
        return render(request, 'reggenqr.html',{'myname':ss})


def delett(request,id):
    oks=qr_model_auth.objects.get(id=id)
    oks.delete()

    return redirect('portfolio')
    
def forgetpass(request):
    return render(request,'forgetpass.html')
def chk_otp(request):
    return render(request,'chk_otp.html')
def change_pass(request):
    return render(request,'change_pass.html')


def update_pass(request):
    if request.method=='POST':
        userrr_email=request.POST['email']
        find_email=User.objects.filter(email=userrr_email)
        if find_email:
            o=''
            totp = str(random.randint(10000,200000))
            o+=totp
            request.session['ottp']=o 
            

        # if request.method=='POST':
        #     cod=request.POST['otpp']
        #     # if code==ott:
        #  messages.success(request,' signup succesfully')
            send_mail(
                        "OTP SparkQR",
                        f"Your OTP is : {o} \nWelcome to our community.We are happy to have you on board.\nThanks \nBest Regards,\nSparkQR",
                        "lunawork04@gmail.com",
                        [userrr_email],
                        fail_silently=False,
                    )


            return render(request,'chk_otp.html')
        else:
            messages.error(request,'User not registered!')
            return redirect('forgetpass')

    else:
        return render(request,'forgetpass.html')
        

        

def ottp(request):
        o=''
        totp = str(random.randint(10000,200000))
        o+=totp
        request.session['ottp']=o 
            

        # if request.method=='POST':
        #     cod=request.POST['otpp']
        #     # if code==ott:
        #  messages.success(request,' signup succesfully')
        send_mail(
                "Travel Diaries Otp",
                f"Your OTP is : {o} Welcome to our community.We are happy to have you on board.Why don't you follow our CEO on instagram https://www.instagram.com/iarrav/ Thanks Regards :Travel Diaries",
                "lunawork04@gmail.com",
                [request.session['email']],
                fail_silently=False,
            )


        return render(request,'chk_otp.html')

def otp_vrify(request):

    if request.method=='POST':
        od=request.POST.get('ottp')

        if od==request.session['ottp']:
            em=request.POST.get('email')
            user=User.objects.get(email=em)
            return render(request,'change_pass.html',{'user':user})

        #  set_pas=make_password(password=request.session['password'])
        #  User.is_active=True
       
            
        else:
            messages.error(request,'Incorrect OTP!')
            return render(request,'chk_otp.html')
        



def gen_pass(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        nuserp=request.POST['New_password']
        cnuserp=request.POST['Cnew_password']
        if nuserp==cnuserp:
         user.password=make_password(nuserp)

         user.save()
         return redirect('signin')
        else:
            messages.error(request,'Passwords do not Match. Please try again!')
            return render(request,'change_pass.html')
        
  
    else:
        return render(request,'change_pass.html')
        
            


        