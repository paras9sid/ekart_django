from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


def home(request):
    # query set
    products = Product.objects.all().filter(is_available=True)

    # dictionary for rendering data in html to frontend
    context = {
        'products': products,
    }
    return render(request,'home.html', context)