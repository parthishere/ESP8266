# Generated by Django 3.2.4 on 2022-04-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_esp8266_mac_unhash'),
    ]

    operations = [
        migrations.AddField(
            model_name='esp8266',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='esp8266',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
