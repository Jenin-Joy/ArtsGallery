# Generated by Django 5.1.4 on 2025-01-11 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0005_initial'),
        ('User', '0018_delete_tbl_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_artwork',
        ),
    ]
