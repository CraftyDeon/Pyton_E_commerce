from django.shortcuts import render, redirect, get_object_or_404
from home.models import Product
from accounts.models import Profile
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
@login_required
def cart(request):
    profile = get_object_or_404(Profile, user=request.user)
    order, created = Order.objects.get_or_create(owner=profile, completed=False)
    order_items = order.orderitem_set.all()
    total_price = sum(item.product.price * item.quantity for item in order_items)
    context = {
        'order': order,
        'order_items': order_items,
        'total_price': total_price,
    }
    return render(request, 'cart/bart.html',context)
