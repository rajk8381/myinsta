from django.shortcuts import render,redirect

from .forms import RegisterForm,LoginForm
from django.contrib import messages
from .models import PublicUser
from django.contrib.auth.models import make_password
from django.contrib.auth import authenticate,login,logout

# SignUp new users | registration page
def register_view(request):
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



def index_view(request):
    return render(request,'index.html')