from django.shortcuts import render

from rest_framework import viewsets
from .model import Customer
from .serializer import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
