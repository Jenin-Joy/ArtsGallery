# Generated by Django 5.1.3 on 2024-12-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_tbl_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_artist',
            name='artist_status',
            field=models.IntegerField(default=0),
        ),
    ]
