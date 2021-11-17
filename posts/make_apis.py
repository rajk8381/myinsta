
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Post,PublicUser
from django.shortcuts import get_object_or_404

class PublicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model =PublicUser
        fields ='__all__'


class PostSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    class Meta:
        model =Post
        fields ='__all__'

    def get_user(self,obj):
        if obj:
            users=PublicUserSerializer(obj.user)
            return users.data
        return ""


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Post

class PostApiList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data={}
        post = Post.objects.filter()
        post_ser =PostSerializer(post, many=True)
        return Response(post_ser.data)
    def post(self,request):
        data={}
        form =PostSerializer(data=request.data)
        if form.is_valid():
            form.save()
            data['success']=form.data
        else:
            data['error']=form.errors
        return Response(data)

class PostApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        data={}
        post = get_object_or_404(Post, pk=pk)
        post_ser =PostSerializer(post)
        return Response(post_ser.data)

    def put(self, request, pk, format=None):
        data={}
        post = get_object_or_404(Post, pk=pk)
        form =PostSerializer(data=request.data,instance=post)
        if form.is_valid():
            form.save()
            data['success']=form.data
        else:
            data['error']=form.errors
        return Response(data)

    def delete(self, request, pk, format=None):
        data={}
        post = get_object_or_404(Post, pk=pk)
        if post:
            post.delete()
            data['success']="Post Deleted Successfully!"
            return Response(data, status=204)
        else:
            data['success'] = "Post id invalid!"

        return Response(data, status=404)
