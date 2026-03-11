from django.shortcuts import render, redirect

from app.forms import ProductForm
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
    form = ProductForm()
    return render(request, 'formulaire.html', {'form': form})


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        Product.objects.create(
            name=form.cleaned_data['name'],
            code=form.cleaned_data['code'],
            price=form.cleaned_data['price'],
            description=form.cleaned_data['description'],
        )
    return redirect('/product')
