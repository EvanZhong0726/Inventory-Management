# Generated by Django 4.0.3 on 2022-05-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_remove_inventoryitem_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
    ]
