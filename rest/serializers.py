from rest_framework import serializers
from rest_framework import viewsets
from .models import Category, Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','description','is_active']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'description', 
            'price', 
            'category', 
            'category_name',
            'is_available', 
            'preparation_time',
            'created_at',
            'updated_at'
        ]
        extra_kwargs = {
            'category': {'write_only': True}
        }
        