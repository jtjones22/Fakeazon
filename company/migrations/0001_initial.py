# Generated by Django 4.1.1 on 2022-09-30 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30, null=True, unique=True, verbose_name='Company Name')),
                ('company_description', models.TextField(max_length=200, null=True, verbose_name='Company Description')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, null=True, verbose_name='Product Name')),
                ('product_price', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Product Price')),
                ('product_description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Product Description')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Company')),
            ],
        ),
    ]