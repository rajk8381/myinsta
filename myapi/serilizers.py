
from rest_framework import serializers
from posts.models import Post
from accounts.models import PublicUser

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =PublicUser
        exclude =('password','is_superuser','user_permissions','groups','username')

class PostSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    post_type=serializers.SerializerMethodField()
    class Meta:
        model =Post
        fields ='__all__'

    def get_post_type(self,obj):
        if obj.post_type=="1":
            return "Public"
        else:
            return "Private"

    def get_user(self,obj):
        if obj.user:
            user_ser =PublicUserSerializer(obj.user)
            return user_ser.data
        else:
            return {}
