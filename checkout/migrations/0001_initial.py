# Generated by Django 3.2.9 on 2022-01-26 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=16)),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(max_length=30)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('town_city', models.CharField(max_length=30)),
                ('address_1', models.CharField(max_length=80)),
                ('address_2', models.CharField(blank=True, max_length=80, null=True)),
                ('address_3', models.CharField(blank=True, max_length=80, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('original_cart', models.TextField(default='')),
                ('stripe_payment_id', models.CharField(default='', max_length=254)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='user_profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_item', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
