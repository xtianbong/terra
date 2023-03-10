# Generated by Django 4.1.3 on 2023-02-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('max_temp', models.IntegerField()),
                ('min_temp', models.IntegerField()),
                ('max_hum', models.IntegerField()),
                ('min_hum', models.IntegerField()),
                ('fan_int', models.IntegerField()),
                ('fan_dur', models.IntegerField()),
            ],
        ),
    ]
