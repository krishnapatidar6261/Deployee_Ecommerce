# Generated by Django 4.2.3 on 2023-08-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0017_product_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('accessories', 'Accessories'), ('Electronics', 'Electronics'), ('Men', 'Men'), ('Women', 'Women'), ('Baby & Kids', 'Baby & Kids'), ('Home & Kitchens', 'Home & Kitchens'), ('Books', 'Books'), ('Other', 'Other')], max_length=50),
        ),
    ]