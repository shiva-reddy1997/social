# Generated by Django 4.0.5 on 2022-07-01 12:37

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]