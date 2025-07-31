from django.db import models

from django.db import models

class ShippingInfo(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.full_name} - {self.pincode}"

