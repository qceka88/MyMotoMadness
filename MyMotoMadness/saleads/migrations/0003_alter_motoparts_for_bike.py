# Generated by Django 4.2.3 on 2023-08-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleads', '0002_motoequipmentgear_city_motoparts_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motoparts',
            name='for_bike',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
