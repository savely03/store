from django.shortcuts import render, redirect, get_object_or_404, reverse
from .cart import Cart
from products_app.models import Product


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    cart.add(product=product, quantity=1)
    return redirect("cart_detail")


def cart_decrease(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    cart.add(product, quantity=-1)
    return redirect("cart_detail")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    products = [item['product'] for item in cart if item['quantity'] < 1]
    while products:
        return redirect(reverse("cart_remove", args=(products.pop().id,)))
    return render(request, 'cart/detail.html', context={'cart': cart})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')
