# Generated by Django 4.2.3 on 2023-10-08 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0009_alter_chinese_chinese_id_alter_guj_gujraj_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chinese',
            old_name='chinese_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='guj',
            old_name='gujraj_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='indian_street',
            old_name='street_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='italian',
            old_name='italian_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='north',
            old_name='north_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='south',
            old_name='south_id',
            new_name='product_id',
        ),
    ]
