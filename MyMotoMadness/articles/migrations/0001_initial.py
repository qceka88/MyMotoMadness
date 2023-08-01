# Generated by Django 4.2.3 on 2023-08-01 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('sub_title', models.CharField(max_length=30)),
                ('article_image', models.ImageField(blank=True, null=True, upload_to='photos/article_photos')),
                ('description', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('article_type', models.CharField(choices=[('News', 'News'), ('Advices', 'Advices')], max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
