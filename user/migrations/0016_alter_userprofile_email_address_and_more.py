# Generated by Django 5.0.4 on 2024-04-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_userprofile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_address',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='national_code',
            field=models.CharField(default='', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=11, null=True),
        ),
    ]
