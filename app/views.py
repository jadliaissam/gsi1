from django.shortcuts import render, redirect

from app.models import Product, Caracteristic


def product_count(request):
    products = Product.objects.all()
    products_count = len(products)
    return render(request, 'index.html', {
        'products_count': products_count,
        'products': products
    })


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    characteristics = Caracteristic.objects.filter(product=product)
    return render(request, 'detail.html', {
        'product': product,
        'characteristics': characteristics
    })


def show_form(request):
    return render(request, 'formulaire.html')

def create_product(request):
    name = request.POST['name']
    code = request.POST['code']
    price = request.POST['price']
    description = request.POST['description']
    Product.objects.create(
        name=name,
        code=code,
        price=int(price),
        description=description
    )
    return redirect('/product')
