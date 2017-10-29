# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='household_audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.ImageField(upload_to='Household_Photos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('HID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Household')),
            ],
        ),
        migrations.CreateModel(
            name='household_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.ImageField(upload_to='Household_Photos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('HID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Household')),
            ],
        ),
        migrations.CreateModel(
            name='household_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.ImageField(upload_to='Household_Photos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('HID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Household')),
            ],
        ),
    ]