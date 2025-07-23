from django.db import models

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    customer = models.CharField(max_length=255) 
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.customer






# class OrderItem(models.model):
#     order_name = models.ForeignKey(Order, on_delete=models.CASCADE)
#     quantity = models.IntegerField()


    # @property
    # def item_subtotal(self):
    #     return self.product.price * self.quantity