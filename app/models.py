from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)


class Caracteristic(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    content = models.TextField()
