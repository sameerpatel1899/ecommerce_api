from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ShippingInfo
from .serializers import ShippingInfoSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

@method_decorator(csrf_exempt, name='dispatch')
class ShippingInfoCreateView(APIView):

    @swagger_auto_schema(request_body=ShippingInfoSerializer)
    def post(self, request):
        serializer = ShippingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
