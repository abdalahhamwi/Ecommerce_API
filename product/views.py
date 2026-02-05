from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(["GET"])
def list_products(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return Response({"products": serializers.data})


@api_view(["GET"])
def get_by_id_product(request, id):
    products = get_object_or_404(Product, id=id)
    serializers = ProductSerializer(products, many=False)
    return Response({"product": serializers.data})