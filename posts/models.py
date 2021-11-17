from django.db import models

# Create your models here.
from accounts.models import PublicUser
class Post(models.Model):
    # user =<ob1>
    #user_id =1
    user=models.ForeignKey(PublicUser, on_delete=models.CASCADE, related_name="post_user")
    image =models.ImageField(upload_to="uploads/posts",default="p.png")
    desc =models.TextField(max_length=1000)
    post_type = models.CharField(max_length=1,
                              choices=(('1', "Public"), ('2', "Private")),
                              default="1")
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,
                                 choices=(
                                     ('1', "Active"),
                                     ('2', "Inactive"),
                                     ('3', "Blocked"),
                                     ('4', "Spam"),
                                 ),
                                 default="1")
