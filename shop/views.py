from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from math import ceil
import  json
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer)


    else:
        order = []

    products = product.objects.all()
    allprods = []    
    catproducts = product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catproducts}
    for cat in cats:
        prod = product.objects.filter(product_category=cat)
        n = len(prod)
        nslides = n//4 +ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])
    params = {'allProds': allprods, 'order':order}
    return render(request, 'index.html', params)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    return render(request, 'header.html', {'order':order})


def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)


    else:
        order = []
    return render(request, 'about.html', {'order':order})
    

def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)


    else:
        order = []

    if request.method =="POST":        
        name = request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name,email=email, phone=phone,desc=desc)
        contact.save()
        
    return render(request, 'contact.html', {'order':order})

# def checkout(request):
    
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer = customer, complete = False)
#         items = order.orderitem_set.all()

#     else:
#         items = {}
#         order = {'get_cart_total':0, 'get_cart_items':0}


    

#     context = {'order':order, 'items':items}

#     return render(request, 'checkout.html', context)



        

def prodview(request, myid):
    # fetch by id

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)


    else:
        order = []

    prod = product.objects.filter(id=myid)
    # print(prod)
    return render(request, 'prodview.html', {'prod':prod[0], 'name':'harshit', 'order':order})

def checkout(request):
    
    if request.user.is_authenticated:
        prod = product.objects.all()
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        # ordereditems = OrderItem.objects.all()
        
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            zipcode = request.POST['zipcode']
            # prod = product.objects.filter(id=)
            # prod_ids = list()
            # print(items.order.complete)
            # for i in ordereditems:
            #     print(i.order.complete)
            #     # prod.stock -= i.quantity
            #     # prod_ids.append(prod.id)
            #     i.order.complete = True
            #     print(i.order.complete)


            checkout = Checkout(customer=customer, name=name, email=email, address=address, city=city, state=state , zipcode=zipcode)
            checkout.save()
            
            # order, created = Order.objects.get_or_create(customer=customer, complete=False)
            # order.complete = True
            
            return redirect('/')

            
    else:
        items = {}
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'order':order, 'items':items}

    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    action = data['action']
    prodcutId = data['productId']


    customer = request.user.customer
    products = product.objects.get(id = prodcutId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=products)

    if action == "add":
        orderItem.quantity = orderItem.quantity+1
        
    elif action =="remove":
        orderItem.quantity = orderItem.quantity-1

    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete() 

    return JsonResponse("Item was added ", safe=False)
     
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False )
        items  = order.orderitem_set.all()
        print(order)
    else:
        items = {}
        order  = {'get_cart_items':0, 'get_cart_total':0}
        return render(request, 'login.html')    
        
    context  = {'items':items, 'order':order}
    return render(request, 'cart.html', context)


# def shipping(request):
# if request.method = "POST":
#     address = request.POST.get('address')
#     city = request.POST.get('city')
#     state = request.POST.get('state')
#     zipcode = request.POST.get('zipcode')
#     shipped = Shipping(address = address, city = city, state = state, zipcode = zipcode)
#     shipped.save()






