# Generated by Django 4.1 on 2022-08-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_cargo_image_cargo_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
