# Generated by Django 4.2.1 on 2023-06-26 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_producto_fecha_ingreso_producto_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_ingreso',
            field=models.DateField(auto_now_add=True),
        ),
    ]
