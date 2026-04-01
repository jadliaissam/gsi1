from django.forms.models import model_to_dict
from django.shortcuts import render, redirect

from app.forms import ProductForm, ContactForm
from app.models import Product, Caracteristic, Message


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


def list_messages(request):
    messages = Message.objects.all()
    return render(request, 'list_messages.html', {'messages': messages})


def show_contact_form(request):
    return render(request, 'contact_htmlform.html')


def handle_contact_form(request):
    name = request.POST['name']
    subject = request.POST['subject']
    email = request.POST['email']
    content = request.POST['content']

    Message.objects.create(name=name, subject=subject, email=email, content=content)
    return redirect('/messages')


def handle_contact_form2(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'form_djangoform.html', {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                name=form.cleaned_data['name'],
                subject=form.cleaned_data['subject'],
                email=form.cleaned_data['email'],
                content=form.cleaned_data['content']
            )
            return redirect('/messages')
        else:
            return render(request, 'form_djangoform.html', {'form': form})


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


def edit_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if request.method == 'GET':
        form = ContactForm(initial=model_to_dict(message))
        return render(request, 'form_djangoform.html', {'form': form})
    else:
        pass
