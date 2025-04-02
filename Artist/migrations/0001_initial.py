# Generated by Django 5.1.3 on 2024-12-18 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0004_tbl_artist_artist_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork_photo', models.FileField(upload_to='Assets/User/Photo/')),
                ('artwork_status', models.IntegerField(default=0)),
                ('artwork_price', models.CharField(max_length=30)),
                ('artwork_description', models.CharField(max_length=50)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_artist')),
            ],
        ),
    ]
