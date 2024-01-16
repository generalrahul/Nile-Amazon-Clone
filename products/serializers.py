from .models import *

from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url
  
    class Meta:
        model = Product
        fields = '__all__'

