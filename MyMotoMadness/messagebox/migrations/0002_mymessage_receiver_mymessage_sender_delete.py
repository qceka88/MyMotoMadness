# Generated by Django 4.2.3 on 2023-08-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagebox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymessage',
            name='receiver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mymessage',
            name='sender_delete',
            field=models.BooleanField(default=False),
        ),
    ]