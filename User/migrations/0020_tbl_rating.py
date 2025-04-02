# Generated by Django 5.1.4 on 2025-01-12 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_artist_artist_status'),
        ('User', '0019_tbl_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_data', models.IntegerField()),
                ('user_name', models.CharField(max_length=500)),
                ('user_review', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_artist')),
            ],
        ),
    ]
