from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import SAFE_METHODS, BasePermission
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
