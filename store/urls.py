from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),

    path("add-to-cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="view_cart"),
    path("remove/<int:pk>/", views.remove_from_cart, name="remove_from_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update/<int:pk>/<str:action>/", views.update_quantity, name="update_quantity"),
    path("api/products/", views.api_products, name="api_products"),
    path("api/products/<int:pk>/", views.api_product_detail, name="api_product_detail"),
]

