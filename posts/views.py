from django.shortcuts import render,redirect

# Create your views here.
from .models import Post

def index_view(request):
    if not request.user.is_authenticated: # user validate login or not if not login user redirectany page
        return redirect('login')
    print("------------------------")

    return render(request,'index.html')
def all_posts_view(request):
    context ={}
    all_post =Post.objects.filter(status="1")
    context['all_post']= all_post
    return render(request,"posts/all_posts.html",context)