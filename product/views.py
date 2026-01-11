from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from .serializers import ProductSerializer

# Create your views here.


@api_view(["GET"])
def list_products(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    print(products)
    return Response({"products": serializers.data})
