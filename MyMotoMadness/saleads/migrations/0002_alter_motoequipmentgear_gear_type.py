# Generated by Django 4.2.3 on 2023-08-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motoequipmentgear',
            name='gear_type',
            field=models.CharField(choices=[('Helmet', 'Helmet'), ('Race Suit One Part', 'Race Suit One Part'), ('Race Suit Two Parts', 'Race Suit Two Parts'), ('Bonnet', 'Bonnet'), ('Boots', 'Boots'), ('Gloves', 'Gloves'), ('Protectors', 'Protectors'), ('Other..', 'Other..')], max_length=20),
        ),
    ]