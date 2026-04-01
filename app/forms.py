from django.forms import *


class ProductForm(forms.Form):
    name = CharField(max_length=100)
    code = CharField(max_length=100)
    description = CharField()
    price = IntegerField()


class ContactForm(forms.Form):
    name = CharField(max_length=100)
    subject = CharField(max_length=100)
    email = EmailField(max_length=100)
    content = CharField(widget=Textarea)
