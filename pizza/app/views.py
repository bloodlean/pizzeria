from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()  
    return render(request, 'base.html', {
        'products': products,
        'categories': categories  
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'category_view.html', {
        'category': category,
        'products': products
    })
