# Generated by Django 3.2.9 on 2022-01-30 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0003_auto_20220130_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='subscription_billing_id',
            new_name='sub_id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='price',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='service',
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SubscriptionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_price', to='subscriptions.price')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='subscriptions.serviceproduct')),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='sub_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_product', to='subscriptions.subscriptionproduct'),
        ),
    ]
