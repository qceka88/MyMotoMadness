# Generated by Django 4.2.3 on 2023-08-19 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagebox', '0002_mymessage_message_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymessage',
            old_name='slug',
            new_name='message_slug',
        ),
    ]