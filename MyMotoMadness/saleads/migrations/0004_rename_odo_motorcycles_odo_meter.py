# Generated by Django 4.2.3 on 2023-08-15 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleads', '0003_alter_motorcycles_odo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motorcycles',
            old_name='odo',
            new_name='odo_meter',
        ),
    ]
