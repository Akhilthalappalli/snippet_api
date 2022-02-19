from rest_framework import serializers, validators
from api.models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = "__all__"


class SnippetsSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SerializerMethodField(read_only='True')
    class Meta:
        model = Snippet
        fields = ['url','id','title', 'tags']

    def get_tags(self,obj):
        return obj.tag.title


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
