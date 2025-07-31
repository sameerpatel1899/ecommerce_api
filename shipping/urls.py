from django.urls import path
from .views import ShippingInfoCreateView

urlpatterns = [
    path('', ShippingInfoCreateView.as_view()),
]
