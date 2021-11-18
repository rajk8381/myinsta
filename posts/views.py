from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .models import Post

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
    post =Post.objects.get(id=pid)
    post.likes.add(request.user)
    post.save()
    msg ="like hua"+str(pid)
    return HttpResponse(msg)