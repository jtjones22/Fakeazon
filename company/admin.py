from django.contrib import admin
from .models import Company, Product
from django.utils.html import format_html
# Register your models here.

# @admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'owner_name', 'created', 'updated')
    def owner_name(self,obj):
        return format_html(f'<a href="/admin/user/myuser/{obj.owner.pk}/change/">{obj.owner.email}</a>')
admin.site.register(Company, CompanyAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'company_name', 'created', 'updated')

    def company_name(self, obj):
        return format_html(f'<a href="/admin/company/company/{obj.company.pk}/change/">{obj.company}</a>')
admin.site.register(Product, ProductAdmin)