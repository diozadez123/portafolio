# Generated by Django 3.2.7 on 2021-09-12 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='stok',
            new_name='stock',
        ),
    ]
