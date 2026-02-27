from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.


@api_view(["GET"])
def list_products(request):
    # Filter
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by("id"))
    # Pagination
    paginator = PageNumberPagination()
    paginator.page_size = 2
    page = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(page, many=True)
    return Response({"products": serializer.data})


@api_view(["GET"])
def get_by_id_product(request, id):
    products = get_object_or_404(Product, id=id)
    serializers = ProductSerializer(products, many=False)
    return Response({"product": serializers.data})
