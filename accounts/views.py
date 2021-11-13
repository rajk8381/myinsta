from django.shortcuts import render

from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import make_password
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
    return render(request,"accounts/login.html")