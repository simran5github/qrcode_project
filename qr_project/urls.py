"""
URL configuration for qr_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from qr_app import views

urlpatterns = [
    path("sim", admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('do',views.do,name='do'),
    path('genqr',views.genqr,name='genqr'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('privacy',views.privacy,name='privacy'),
    path('signin',views.signin,name='signin'),
    path('forgetpass',views.forgetpass,name='forgetpass'),
    path('chk_otp',views.chk_otp,name='chk_otp'),
    path('change_pass',views.change_pass,name='change_pass'),
    path('signup',views.signup,name='signup'),
    path('logout',views.loogout,name='logout'),
    path('Take_Review',views.Take_Review,name='Take_Review'),
    path('search_qro',views.search_qro,name='search_qro'),
    path('termsofuse',views.termsofuse,name='termsofuse'),
    path('ottp', views.ottp , name='ottp'),
    path('gen_pass/<int:id>', views.gen_pass , name='gen_pass'),
    path('update_pass', views.update_pass , name='update_pass'),

    path('otp_vrify', views.otp_vrify , name='otp_vrify'),

    #registered users#
    path('regindex',views.regindex,name='regindex'),
    path('regabout',views.regabout,name='regabout'),
    path('regcontact',views.regcontact,name='regcontact'),
    path('regdo',views.regdo,name='regdo'),
    path('reggenqr',views.reggenqr,name='reggenqr'),
    path('regtermsofuse',views.regtermsofuse,name='regtermsofuse'),
    path('regprivacy',views.regprivacy,name='regprivacy'),
    path('reg_Take_Review',views.reg_Take_Review,name='reg_Take_Review'),
    path('delete/<int:id>',views.delett,name='delete'),


    ##

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


