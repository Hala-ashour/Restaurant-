from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    category = models.ForeignKey(
        Category, 
        related_name='products',
        on_delete=models.SET_NULL,
        null=True
    )
    is_available = models.BooleanField(default=True)
    preparation_time = models.PositiveIntegerField(
        help_text="Preparation time in minutes",
        default=15
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

    class Meta:
        ordering = ['-created_at']