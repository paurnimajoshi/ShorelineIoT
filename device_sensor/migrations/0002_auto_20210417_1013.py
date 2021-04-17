# Generated by Django 3.2 on 2021-04-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_sensor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='unique_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='unique_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]