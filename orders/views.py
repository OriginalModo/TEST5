from django.shortcuts import render, redirect
from .models import Order, Product
from .tasks import prepare_order


def order_create(request):
    if request.method == 'POST':
        person_name = request.POST['personName']
        product_id = request.POST['productId']
        quantity = request.POST['quantity']

        product = Product.objects.get(id=product_id)

        order = Order.objects.create(personName=person_name)
        order.products.add(product, through_defaults={'quantity': quantity})

        prepare_order.delay(order.id)

        return redirect('order_list')

    products = Product.objects.all()
    return render(request, 'orders/order_form.html', {'products': products})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})