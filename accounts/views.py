from django.shortcuts import render


# SignUp new users | registration page
def register_view(request):
    return render(request,"accounts/register.html")

def login_view(request):
    return render(request,"accounts/login.html")