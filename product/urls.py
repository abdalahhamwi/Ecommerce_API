from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.list_products, name="list_products"),
    path("products/<int:id>/", views.get_by_id_product, name="get_by_id_product"),
]
