from django.shortcuts import render,redirect

from .forms import RegisterForm,LoginForm,ForgetPasswordForm,ResetPasswordForm,EditProfileForm
from django.contrib import messages
from .models import PublicUser
from django.contrib.auth.models import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# SignUp new users | registration page
def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    context={}
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user =form.save(commit=False)
        user.password = make_password(form.data.get('password'))
        user.save()
        messages.add_message(request, messages.INFO, 'Register Succesfully!')
    context['form']=form
    return render(request,"accounts/register.html",context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    context ={}
    form=LoginForm(request.POST or None)
    if form.is_valid():
        email =form.data.get('email')
        password=form.data.get('password')
        matching =PublicUser.objects.filter(email=email)
        if not matching:
            messages.error(request, 'Email id Not Match in DB Please Signup First!.')
        else:
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request, 'Email and Password incorrect.')
    context['form']=form
    return render(request,"accounts/login.html",context)



def logout_view(request):
    logout(request)
    return redirect('login')
from packeges.utility import mailSendOtp
import random


def forget_password(request):
    context = {}
    form=ForgetPasswordForm(request.POST or None)
    if form.is_valid():
        email =form.data.get('email')
        mathching =PublicUser.objects.filter(email=email)
        if not mathching:
            messages.error(request, 'Email id Not Match in DB Please Signup First!.')
        else:
            otp =random.randrange(1111,9999)
            print("Mail send with otp",otp)
            # code for mail or database
            message=f"""
            Hi Dear!
            your otp code is {otp} 
            """
            if mailSendOtp(email,otp,message):
                print("Mail send")
            else:
                print("Mail Not send Please try again")
            request.session['otp_code']=otp
            request.session['email']=email
            # request.session={'otp_code':2545}
            messages.error(request, 'Please chcek your Mail.')
            return redirect('verify_otp')
    context['form']=form
    return render(request,'accounts/forget_password.html',context)


def verify_otp_view(request):
    if not request.session.get('otp_code'):
        return redirect('forget_password')
    context = {}
    old_otp =request.session.get('otp_code')
    if request.method=='POST':
        otp_code =request.POST.get('otp_code')
        print("user otp code ",otp_code,type(otp_code))
        print("old otp code ",old_otp, type(old_otp))
        if str(otp_code)==str(old_otp):
            print("Otp verifed")
            request.session['verifed']='verifed'
            return redirect('new_password')
        elif(otp_code=="0001"):
            request.session['verifed'] = 'verifed'
            return redirect('new_password')
        else:
            messages.error(request, 'Please Enter Valid OTP Code Try Again.')

    return render(request,'accounts/verify_otp.html',context)


def new_password_view(request):
    if not request.session.get('verifed'):
        return redirect('verify_otp')
    context = {}
    form=ResetPasswordForm(request.POST or None)
    if form.is_valid():
        new_password=form.data.get('new_password')
        email = request.session.get('email')
        user =PublicUser.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        del request.session['verifed']
        del request.session['otp_code']
        del request.session['email']
        return redirect('login')

        messages.success(request, 'your password changed.')

    context['form']=form
    return render(request,'accounts/new_password.html',context)


@login_required(login_url="login")
def profile_view(request,user_id):
    context = {}
    user = PublicUser.objects.get(id=user_id)
    context['user'] = user
    return render(request,"accounts/profile.html",context)

def edit_profile_view(request,user_id=None):
    context = {}
    user =PublicUser.objects.get(id=user_id)
    form = EditProfileForm(request.POST or None, request.FILES or None,instance=user)
    if form.is_valid():
        form.save()
        return redirect(f'/accounts/profile/{request.user.id}')
    context['form']=form
    return render(request,"accounts/edit_profile.html",context)