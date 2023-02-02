from django.shortcuts import render, reverse, redirect
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem, Order, ConfirmOrder
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    if not request.user.is_authenticated:
        return redirect("login")
    form = OrderForm()
    cart = Cart(request)
    sm = sum(item['total_price'] for item in cart)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if len(cart) == 0:
            messages.error(request, "Ваша корзина пуста. Пожалуйста добавьте товары.")
            return render(request, "order/order_create.html", context={'form': form, "cart": cart})
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = sm
            order.save()
            reverse_url = reverse("make_order", args=(order.pk,))
            return redirect(reverse_url)
    return render(request, 'order/order_create.html', context={'form': form, 'cart': cart, "sm": sm})


@login_required
def make_order(request, pk):
    cart = Cart(request)
    order = Order.objects.get(pk=pk)
    total = sum(item['total_price'] for item in cart)
    if request.method == "POST":
        confirm_order = ConfirmOrder.objects.create(
            user=order.user,
            first_name=order.first_name,
            last_name=order.last_name,
            email=order.email,
            address=order.address,
            total_price=order.total_price,
        )
        for item in cart:
            OrderItem.objects.create(
                order=confirm_order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'],
            )
        for item in cart:
            product = item['product']
            product.quantity -= item['quantity']
            product.save()
        cart.clear()
        order.delete()
        return redirect("success")
    return render(request, "order/order.html", context={"order": order, "cart": cart, "total": total})


@login_required
def orders(request):
    orders = ConfirmOrder.objects.filter(user=request.user).all()
    return render(request, "order/orders.html", context={"orders": orders})


def success(request):
    return render(request, "order/success.html")


@login_required
def order_watch(request, pk):
    orders = OrderItem.objects.filter(order__pk=pk)
    order_id = ConfirmOrder.objects.get(pk=pk).id
    sm = sum(order.get_cost() for order in orders)
    return render(request, "order/order_watch.html", context={"orders": orders, "sm": sm, "order_id": order_id})
