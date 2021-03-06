# Generated by Django 3.2.9 on 2022-01-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_delete_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceproduct',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='_last_payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='_next_payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='_payment_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_billing_id',
            field=models.CharField(default='missing_id', max_length=50),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_status',
            field=models.CharField(choices=[('active', 'Current'), ('past_due', 'Past Due'), ('canceled', 'Cancelled'), ('none', 'None'), ('incomplete', 'Incomplete'), ('incomplete_expired', 'Incomplete Expired'), ('trialing', 'Trialing'), ('unpaid', 'Unpaid')], default='incomplete', max_length=25),
        ),
        migrations.AlterField(
            model_name='serviceproduct',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
