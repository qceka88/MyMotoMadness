# Generated by Django 4.2.3 on 2023-07-30 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleads', '0003_alter_motoequipmentimages_moto_equipment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motoequipmentimages',
            old_name='images',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='motopartsimages',
            old_name='images',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='motorcycleimages',
            old_name='images',
            new_name='image',
        ),
    ]
