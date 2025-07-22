from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
