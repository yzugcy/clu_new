# Generated by Django 4.2.11 on 2024-03-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tour Title')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='tours/')),
                ('duration', models.IntegerField(default=0, verbose_name='Duration in minutes')),
                ('scenes', models.IntegerField(default=0, verbose_name='Scenes')),
                ('location', models.CharField(max_length=255, null=True, verbose_name='Location')),
                ('latitude', models.CharField(max_length=255, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=255, null=True, verbose_name='Longitude')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
