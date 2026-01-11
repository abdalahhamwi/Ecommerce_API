from django.urls import path
from .views import list_products

urlpatterns = [
    path("products/", view=list_products, name="list_products"),
]
