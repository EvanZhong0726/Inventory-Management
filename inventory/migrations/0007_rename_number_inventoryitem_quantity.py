# Generated by Django 4.0.3 on 2022-05-21 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_inventoryitem_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='number',
            new_name='quantity',
        ),
    ]
