# Generated by Django 5.0.7 on 2024-07-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two_way_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='receivedAt',
            field=models.CharField(max_length=255),
        ),
    ]
