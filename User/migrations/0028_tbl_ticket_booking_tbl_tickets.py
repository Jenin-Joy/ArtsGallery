# Generated by Django 5.1.4 on 2025-02-09 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_event'),
        ('Guest', '0004_tbl_artist_artist_status'),
        ('User', '0027_remove_tbl_tickets_booking_delete_tbl_ticket_booking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ticket_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.IntegerField(default=0)),
                ('booking_totalamount', models.CharField(max_length=50, null=True)),
                ('booking_time', models.TimeField()),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_artist')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_ticket_booking')),
            ],
        ),
    ]
