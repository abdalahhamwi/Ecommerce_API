from django.urls import path
from . import api

urlpatterns = [
    path("products/", api.list_products, name="list_products"),
    path("products/<int:id>/", api.get_by_id_product, name="get_by_id_product"),
    
]
