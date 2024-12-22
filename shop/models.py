from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    full_name= models.CharField(max_length=100, default=None)
    address = models.CharField(max_length=255, default=None)
    phone = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


