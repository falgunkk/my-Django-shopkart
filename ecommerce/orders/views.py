
from django.shortcuts import render
from .models import OrderItem
from .models import Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if request.user.is_authenticated:
               order.user_id=request.user.id
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

def order_details(request):
    user = request.user
    orders = Order.objects.filter(user_id=user.id)
    items = OrderItem.objects.filter(order_id__in=orders.values_list('id'))
    order_detail = []
    order_no=0
    for order in orders:
        order_no+=1
        items = OrderItem.objects.filter(order_id=order.id).first()
        total_of_order = items.quantity*items.price
        order_detail.append({'order': order, 'items': items, 'total': total_of_order, 'order_no': order_no})
    # import pdb; pdb.set_trace()
    print order_detail
    return render(request, 'orders/order/order_details.html', {'order_detail': order_detail})

def test(request):
    dicts_array = [{'order':"first", 'items': "second"},{'order':"third", 'items': "fourth"}]
    print dicts_array
    return render(request, 'orders/order/test.html', {'dicts_array': dicts_array})
