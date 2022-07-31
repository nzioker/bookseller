from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}

    all_books = Book.objects.all()
    context = {'all_books': all_books, 'order':order}
    return render(request, 'index.html', context)

def products(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}

    all_books = Book.objects.all()
    context = {'all_books': all_books, 'order':order}
    return render(request, 'products.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}

    context = {'items':items, 'order':order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}

    context = {'items':items, 'order':order}
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    bookId = data['productId']
    action = data['action']
    print(f'BookId {bookId}: Action: {action}')

    customer = request.user.customer
    product = Book.objects.get(id=bookId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, book=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Data well received", safe=False)

def processOrder(request):
    data = json.loads(request.body)
    print(f"Data: {data}" )
    return JsonResponse("Order processed", safe=False)