from django.shortcuts import render, redirect,get_object_or_404
# Create your views here.
from .models import Product
from accounts.models import Profile
from cart.models import OrderItem,Order
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
def view (request,pk):
    form = get_object_or_404(Product, pk=pk)
    return render(request, 'home/viewer.html', {'form': form})
def index(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_obj = paginator.get_page(page)
    return render(request, 'home/home.html', {'page_obj': page_obj,'query': query})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    profile = get_object_or_404(Profile, user=request.user)
    order, created = Order.objects.get_or_create(owner=profile, completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    quantity = int(request.POST.get('quantity', 1))
    order_item.quantity += quantity
    order_item.save()
    return redirect('kart')
@login_required
def remove_from_cart(request, item_id):
    order_item = get_object_or_404(OrderItem, id=item_id)
    profile = get_object_or_404(Profile, user=request.user)
    order = get_object_or_404(Order, owner=profile, completed=False)
    if order_item.order == order:
        if order_item.quantity<=1:
            order_item.delete()
        else:
            order_item.quantity-=1
            order_item.save()
    return redirect('kart')
@login_required
def remove_all_from_cart(request, item_id):
    order_item = get_object_or_404(OrderItem, id=item_id)
    profile = get_object_or_404(Profile, user=request.user)
    order = get_object_or_404(Order, owner=profile, completed=False)
    if order_item.order == order:
        order_item.delete()
    return redirect('kart')