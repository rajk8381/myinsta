from django.urls import path
from . import views
urlpatterns =[
    path('',views.index_view, name='index'),
    path('all_posts/',views.all_posts_view, name='all_posts'),
    path('addPost/',views.save_post_view, name='add_post'),
    path('post_like/<pid>/',views.post_like_view, name='post_like'),
    path('post_details/<pid>/',views.posts_details_view, name='post_details'),
   ]