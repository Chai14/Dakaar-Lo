# Generated by Django 4.2.3 on 2023-10-10 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0010_rename_chinese_id_chinese_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
