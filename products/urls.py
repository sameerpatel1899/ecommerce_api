from django.urls import path
from .views import ProductListCreateView, ProductDetailView

urlpatterns = [
    path('', ProductListCreateView.as_view()),      # GET + POST /products/
    path('<int:pk>/', ProductDetailView.as_view()), # GET /products/1/
]
