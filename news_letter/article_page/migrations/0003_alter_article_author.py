# Generated by Django 3.2.9 on 2022-01-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_page', '0002_auto_20220107_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(related_name='authors', to='article_page.Author'),
        ),
    ]