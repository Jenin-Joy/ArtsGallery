# Generated by Django 5.1.3 on 2024-12-07 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_subcategory',
            old_name='tbl_category',
            new_name='category',
        ),
    ]
