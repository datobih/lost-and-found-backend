# Generated by Django 5.1.1 on 2024-11-25 01:23

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=14658384932, max_length=12, unique=True, validators=[accounts.models.validate_phone_number]),
            preserve_default=False,
        ),
    ]
