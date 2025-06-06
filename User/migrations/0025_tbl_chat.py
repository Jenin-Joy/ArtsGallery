# Generated by Django 5.1.4 on 2025-01-26 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_artist_artist_status'),
        ('User', '0024_delete_tbl_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_content', models.CharField(max_length=500)),
                ('chat_time', models.DateTimeField()),
                ('chat_file', models.FileField(upload_to='ChatFiles/')),
                ('artist_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_from', to='Guest.tbl_artist')),
                ('artist_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_to', to='Guest.tbl_artist')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='Guest.tbl_user')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='Guest.tbl_user')),
            ],
        ),
    ]
