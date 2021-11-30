
from django.urls import path
from .views import PostAPI,UserAPI,CustomAuthToken
from rest_framework.authtoken import views
urlpatterns =[
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/post/',PostAPI.as_view()),
    path('api/user/',UserAPI.as_view()),
]