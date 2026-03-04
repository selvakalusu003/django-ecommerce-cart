from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, Order, OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    return JsonResponse({
        "message": "Product added to cart!"
    })

@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = CartItem.objects.filter(cart=cart)

    total = 0
    for item in items:
        total += item.product.price * item.quantity

    return render(request, "store/cart.html", {
        "items": items,
        "total": total
    })

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.delete()

    return redirect("view_cart")

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        return redirect("product_list")

    cart_items = CartItem.objects.filter(cart=cart)

    # ⚠️ Check stock before ordering
    for item in cart_items:
        if item.quantity > item.product.stock:
            return render(request, "store/cart.html", {
                "items": cart_items,
                "error": f"{item.product.name} does not have enough stock!"
            })

    total_price = 0

    for item in cart_items:
        total_price += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        total_price=total_price
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price * item.quantity
        )

        item.product.stock -= item.quantity
        item.product.save()

    cart_items.delete()

    return redirect("product_list")

@login_required
def update_quantity(request, pk, action):
    cart_item = get_object_or_404(CartItem, pk=pk)

    if action == "increase":
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1

    elif action == "decrease":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1

    cart_item.save()

    return redirect("view_cart")

@api_view(["GET"])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def api_product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
