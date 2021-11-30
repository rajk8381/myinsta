from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# AbstractUser  username,password,email,is_staff,login,
# AbstractBaseUser user define files permission

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import UserManager
class PublicUser(AbstractUser):
    username =models.CharField(max_length=100, null=True,blank=True)
    image =models.ImageField(upload_to="uploads/photos", default="a.png")
    mobile=models.CharField(max_length=10, unique=True,null=True,blank=True)
    email=models.EmailField(max_length=200,unique=True)
    about_me=models.TextField(blank=True,null=True)
    dob=models.DateTimeField(null=True,blank=True)
    gender=models.CharField(max_length=1,
                            choices=(('1',"Male"),('2',"Female")),
                            default="")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


    def myusername(self):
        email=str(self.email).split("@")
        try:
            username =email[0]
        except:
            username = ""
        return username



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


