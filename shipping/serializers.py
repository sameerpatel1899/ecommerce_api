from rest_framework import serializers
from .models import ShippingInfo

class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInfo
        fields = '__all__'
