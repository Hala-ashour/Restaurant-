from django.shortcuts import render
from .models import Order
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet 
from .serializers import OrderSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.



# class orderviewset(viewsets.ModelViewSet):
#     page = 5
#     paginator = PageNumberPagination()
#     paginator.page_size=page
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer






class OrderPagination(PageNumberPagination):
    page_size = 5

class orderviewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination















class orderrrr(viewsets.ModelViewSet):
    pass
