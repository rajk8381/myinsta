from django.urls import path

from . import views
urlpatterns =[
    path('register/',views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('forget_password/',views.forget_password, name='forget_password'),
    path('new_password/',views.new_password_view, name='new_password'),
    path('verify_otp/',views.verify_otp_view, name='verify_otp'),

]