# Generated by Django 4.2.3 on 2023-08-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motousermodel',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='photos/profile_pictures'),
        ),
    ]
