from django.shortcuts import render,redirect,HttpResponse
from .models import Post,Follow,Comment
from accounts.models import PublicUser
def index_view(request):
    if not request.user.is_authenticated: # user validate login or not if not login user redirectany page
        return redirect('login')
    return render(request,'index.html')

def all_posts_view(request):
    context ={}
    all_post =Post.objects.filter().order_by("-id")
    context['all_post']= all_post
    return render(request,"posts/all_posts.html",context)

def posts_details_view(request,pid=None):
    context ={}
    one_post =Post.objects.get(pk=pid)
    context['post']= one_post
    return render(request,"posts/post_details.html",context)

def follow_list_view(request,pid=None):
    context ={}
    # followers=Follow.objects.filter(user=request.user).values_list('follow_user',flat=True)
    # users =PublicUser.objects.filter().exclude(pk=request.user.pk).exclude(id__in=followers)


    following =Follow.objects.filter(follow_user_id=request.user.id).values_list("user_id", flat=True)

    users =PublicUser.objects.exclude(id=request.user.id).exclude(id__in=following)

    context['users']= users
    context['count']= users.count()
    return render(request,"posts/follow_list.html",context)


def save_post_view(request):
    image=request.FILES.get("image")
    desc=request.POST.get("desc")
    p =Post()
    p.user=request.user
    p.image=image
    p.desc=desc
    p.save()
    message1 ='<h4 class="text-success">Form save successfully!</h1>'
    return HttpResponse(message1)

def post_like_view(request,pid=None):
    msg = "like Post Successfully!"
    post =Post.objects.get(id=pid)
    already =post.likes.filter(pk=request.user.id)
    if not already:
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
    return HttpResponse(msg)

def follow_unfollow(request,user_id=None):
    msg = "Follow Successfully!"
    followed =Follow.objects.filter(user_id=user_id,follow_user=request.user)
    if followed:
        followed[0].delete()
        msg = "Un-Follow Successfully!"
    else:
        Follow.objects.create(user_id=user_id,follow_user=request.user)
        msg = "Follow Successfully!"
    return HttpResponse(msg)


def friend_list(request):
    context = {}
    followers = Follow.objects.filter(user=request.user).values_list('follow_user', flat=True)
    users = PublicUser.objects.filter(id__in=followers).exclude(pk=request.user.pk)
    context['users'] = users

    return render(request,'posts/friendlist.html',context)





# test

def text_api(request):
    return render(request,'home.html')