from django.forms import *


class ProductForm(forms.Form):
    name = CharField(max_length=100)
    code = CharField(max_length=100)
    description = CharField()
    price = IntegerField()
