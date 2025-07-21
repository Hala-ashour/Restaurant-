from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  
            return True
        return request.user.is_authenticated and (
            request.user.is_staff or getattr(request.user, 'role', '') == 'manager'
        )
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrManager()]
        return [IsAuthenticated()]  


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']
    
    @action(detail=True, methods=['GET'], url_path='check-availability')
    def check_availability(self, request, pk=None):
        
        product = self.get_object()
        return Response({
            'product_id': product.id,
            'product_name': product.name,
            'is_available': product.is_available,
            'message': 'Available for order' if product.is_available else 'Currently unavailable'
        }, status=status.HTTP_200_OK)

