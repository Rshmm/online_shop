# Generated by Django 5.0.4 on 2024-05-25 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_address_street'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='street',
            new_name='full_address',
        ),
    ]
