from django.db import models

from django.db import models
from cart.models import CartItem

class Order(models.Model):  
    items = models.ManyToManyField(CartItem)
    total_amount = models.FloatField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - ₹{self.total_amount}"

