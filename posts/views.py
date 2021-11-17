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