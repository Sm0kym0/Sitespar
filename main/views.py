from django.shortcuts import render
from .models import Store

def home(request):
    return render(request, 'main/home.html')



def store_list(request):
    query = request.GET.get('q', '')
    kitchen = request.GET.get('kitchen') == 'on'
    bakery = request.GET.get('bakery') == 'on'
    delivery = request.GET.get('delivery') == 'on'

    stores = Store.objects.all()

    if query:
        stores = stores.filter(city__icontains=query) | stores.filter(district__icontains=query)

    if kitchen:
        stores = stores.filter(has_kitchen=True)
    if bakery:
        stores = stores.filter(has_bakery=True)
    if delivery:
        stores = stores.filter(has_delivery=True)

    context = {
        'stores': stores,
        'query': query,
        'filters': {
            'kitchen': kitchen,
            'bakery': bakery,
            'delivery': delivery
        }
    }
    return render(request, 'main/stores.html', context)

from .models import Product

def product_list(request):
    category = request.GET.get('category')
    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    return render(request, 'main/catalog.html', {'products': products})

def about(request):
    return render(request, 'main/about.html')


from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')


        print(f"Новое сообщение: {name} ({email}): {message}")

        messages.success(request, 'Ваше сообщение отправлено. Спасибо!')

    return render(request, 'main/contacts.html')
