from django.db import models
from user.models import MyUser
# Create your models here.

class Company(models.Model):
    owner = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name='Owner', null=True, blank=True)
    company_name = models.CharField(max_length=30,null=True, verbose_name="Company Name", unique=True)
    company_description = models.TextField(max_length=200, null=True, verbose_name="Company Description", blank=False)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.company_name



class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=False,  verbose_name='Company')
    product_name = models.CharField(max_length=50, blank=False, null=True, verbose_name='Product Name')
    product_price = models.DecimalField(max_digits=6, decimal_places=0, blank=False, null=True,  verbose_name='Product Price')
    product_description = models.TextField(max_length=200, null=True, verbose_name="Product Description", blank=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product_name