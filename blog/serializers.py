

from rest_framework import serializers
from .models import *
class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True ,allow_blank=False , allow_null=False , max_length=128)
    cover = serializers.CharField(required=True ,allow_blank=False , allow_null=False , max_length=256)
    content = serializers.CharField(required=True ,allow_blank=False , allow_null=False , max_length=2048)
    created_at = serializers.DateTimeField(required=True ,allow_null=False)