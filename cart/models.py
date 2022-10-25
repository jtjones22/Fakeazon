from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

from company.models import Product
from user.models import MyUser
# Create your models here.


class Cart(models.Model):
    customer = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Product)