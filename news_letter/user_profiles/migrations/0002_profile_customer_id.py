# Generated by Django 3.2.9 on 2022-01-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='customer_id',
            field=models.CharField(default='invalid_id', max_length=50),
        ),
    ]