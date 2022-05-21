# Generated by Django 4.0.3 on 2022-05-19 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('image', models.ImageField(blank=True, default='/default.png', null=True, upload_to='')),
                ('company', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='company',
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='name',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
    ]
