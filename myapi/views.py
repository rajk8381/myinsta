from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from accounts.models import PublicUser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serilizers import PostSerializer,PublicUserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class PostAPI(APIView):

    def get(self,request):
        context ={}
        posts_list = Post.objects.all()
        ser_post =PostSerializer(posts_list,many=True)
        context['count'] = len(ser_post.data)
        context['message'] = "Post Listing"
        context['list']=ser_post.data
        return Response(context,status=status.HTTP_200_OK)

class UserAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        context ={}
        user_list = PublicUser.objects.all()
        ser_user =PublicUserSerializer(user_list,many=True)
        context['count'] = len(ser_user.data)
        context['message'] = "Post Listing"
        context['list']=ser_user.data
        return Response(context,status=status.HTTP_200_OK)
