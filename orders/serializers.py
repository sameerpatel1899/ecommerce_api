from rest_framework import serializers
from .models import Order
from cart.serializers import CartItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'total_amount', 'status', 'created_at']
