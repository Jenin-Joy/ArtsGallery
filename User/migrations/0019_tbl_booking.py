# Generated by Django 5.1.4 on 2025-01-11 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0007_initial'),
        ('Guest', '0004_tbl_artist_artist_status'),
        ('User', '0018_delete_tbl_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.IntegerField(default=0)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artist.tbl_artwork')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
