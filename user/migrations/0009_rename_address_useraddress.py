# Generated by Django 5.0.2 on 2024-04-07 15:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_rename_fisrt_name_userprofile_first_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='UserAddress',
        ),
    ]
