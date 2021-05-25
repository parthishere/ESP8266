# Generated by Django 3.2.3 on 2021-05-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esp8266',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('led1', models.BooleanField(default=False)),
                ('led2', models.BooleanField(default=False)),
                ('led3', models.BooleanField(default=False)),
                ('led4', models.BooleanField(default=False)),
                ('pot', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
