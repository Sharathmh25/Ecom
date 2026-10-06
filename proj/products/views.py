from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Products
from .serializers import ProductsSerializers
from rest_framework.filters import SearchFilter
from .paginations import CustomPagination
class products(ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductsSerializers
    filter_backends=[SearchFilter]
    search_fields=['category']
    pagination_class=CustomPagination
class Products(RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductsSerializers
    lookup_field='id'
