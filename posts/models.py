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
    likes =models.ManyToManyField(PublicUser, related_name="like_post",null=True,blank=True)

    # likes=[1,2,5,5]
    # class like_post():
    #     user =models.ForeignKey(PublicUser, on_delete=models.CASCADE, related_name="post_user")
    #     post =models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_user")
# user=PublicUser.objects.get(id=2)
# user.like_post.filter()


class Comment(models.Model):
    user=models.ForeignKey(PublicUser, on_delete=models.CASCADE, related_name="comment_user")
    post =models.ForeignKey(Post, on_delete=models.CharField, related_name='comment_post')
    comment=models.CharField(max_length=2000)
    created_at =models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=True)


# table=commnet
# user_id =5
# post_id =1
# created_at=date(22/-2021)
# status=1


"""
Database Relationship in tables (maltipal table)
one-to-one  dublicate entry not accepted
one-to-many dublicate entry accepted but only one entry at a time
many to many dublicate entry not accepted but matlipal eny posible

how to make relation in table


primarykey=unique key
ForeignKey=reapeat value accecpt


join()
inner join
outer join
cross
self

"""