from django.db import models
from home.models import Product
from accounts.models import Profile
# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)  # Add this line
    def __str__(self):
        return f"Order {self.id} by {self.owner.user.username}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)  # Adjust default as needed
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

