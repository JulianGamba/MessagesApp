# Generated by Django 5.0.7 on 2024-07-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two_way_messages', '0002_alter_result_receivedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='result',
            name='channel',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='result',
            name='destination',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='result',
            name='event',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='result',
            name='sender',
            field=models.CharField(max_length=255),
        ),
    ]
