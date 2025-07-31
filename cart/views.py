from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import Http404

@method_decorator(csrf_exempt, name='dispatch')
class CartListView(APIView):
    def get(self, request):
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class CartAddView(APIView):
    @swagger_auto_schema(request_body=CartItemSerializer)
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            product = Product.objects.get(id=product_id)
            if product.stock < quantity:
                return Response({'error': 'Not enough stock'}, status=400)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# @method_decorator(csrf_exempt, name='dispatch')
# class CartUpdateView(APIView):
#     def put(self, request, pk):
#         try:
#             item = CartItem.objects.get(pk=pk)
#         except CartItem.DoesNotExist:
#             return Response({'error': 'Item not found'}, status=404)
#         serializer = CartItemSerializer(item, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class CartUpdateView(APIView):

    @swagger_auto_schema(request_body=CartItemSerializer)
    def put(self, request, pk):
        try:
            item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found'}, status=404)

        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class CartDeleteView(APIView):
    def delete(self, request, pk):
        try:
            item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found'}, status=404)
        item.delete()
        return Response({'message': 'Deleted successfully'}, status=204)
