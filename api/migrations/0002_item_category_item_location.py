# Generated by Django 5.1.1 on 2024-12-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
