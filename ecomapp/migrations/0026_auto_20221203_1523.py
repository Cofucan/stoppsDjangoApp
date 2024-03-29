# Generated by Django 3.2.5 on 2022-12-03 13:23

from django.db import migrations, models
import django.db.models.base
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0025_alter_product_productowneremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('MOMO', 'momo'), ('ESEWA', 'esewa')], default='Cash On Delivery', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='productowneremail',
            field=models.CharField(default=' ', max_length=300, verbose_name=django.db.models.base.Model.get_deferred_fields),
        ),
    ]
