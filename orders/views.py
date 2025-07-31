from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from cart.models import CartItem
from .serializers import OrderSerializer

@method_decorator(csrf_exempt, name='dispatch')
class OrderCreateView(APIView):
    def post(self, request):
        cart_items = CartItem.objects.all()
        if not cart_items:
            return Response({'error': 'Cart is empty'}, status=400)
        total = sum([item.product.price * item.quantity for item in cart_items])
        order = Order.objects.create(total_amount=total)
        order.items.set(cart_items)
        order.save()
        CartItem.objects.all().delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)

class OrderDetailView(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=404)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

