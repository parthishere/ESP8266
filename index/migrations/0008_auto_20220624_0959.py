# Generated by Django 3.2.4 on 2022-06-24 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('index', '0007_rename_username_esp8266_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField(default=True)),
                ('name', models.CharField(default='led', max_length=120)),
                ('value', models.IntegerField(blank=True, default='0', null=True)),
                ('unique_id', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='esp8266',
            name='led1',
        ),
        migrations.RemoveField(
            model_name='esp8266',
            name='led2',
        ),
        migrations.RemoveField(
            model_name='esp8266',
            name='led3',
        ),
        migrations.RemoveField(
            model_name='esp8266',
            name='led4',
        ),
        migrations.RemoveField(
            model_name='esp8266',
            name='mac_unhash',
        ),
        migrations.RemoveField(
            model_name='esp8266',
            name='pot',
        ),
        migrations.RemoveField(
            model_name='esp8266',
            name='updated',
        ),
        migrations.AddField(
            model_name='esp8266',
            name='unique_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='esp8266',
            name='mac',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='esp8266',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile'),
        ),
        migrations.CreateModel(
            name='ChangeTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('Appliences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.applience')),
            ],
        ),
        migrations.AddField(
            model_name='applience',
            name='esp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.esp8266'),
        ),
    ]