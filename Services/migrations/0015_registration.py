# Generated by Django 5.0 on 2023-12-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0014_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
