# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 19:29
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Crop', models.CharField(max_length=50)),
                ('Yield', models.FloatField(null=True)),
                ('Extent', models.FloatField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('FID', models.AutoField(primary_key=True, serialize=False)),
                ('plot', django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326)),
                ('area', models.FloatField(default=0.0)),
                ('DateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='farm_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.ImageField(upload_to='Farm_Photos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('FID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='farm_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_name', models.FileField(upload_to='Farm_Videos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('FID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('HID', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(null=True)),
                ('number_of_member', models.IntegerField(null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(1, 1), null=True, srid=4326)),
                ('monthly_income', models.IntegerField(null=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('relation', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('HID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Household')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(choices=[('S', 'Summer'), ('W', 'Winter'), ('M', 'Monsoon')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('SID', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=30)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(1, 1), null=True, srid=4326)),
                ('storage', models.FloatField(null=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='storage_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.ImageField(upload_to='Storage_Photos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('SID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='storage_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_name', models.FileField(upload_to='Storage_Videos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('SID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('WID', models.AutoField(primary_key=True, serialize=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(1, 1), null=True, srid=4326)),
                ('average_yield', models.DecimalField(decimal_places=4, max_digits=7)),
                ('depth', models.FloatField(null=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('FID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='well_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.ImageField(upload_to='Well_Photos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('WID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Well')),
            ],
        ),
        migrations.CreateModel(
            name='well_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_name', models.FileField(upload_to='Well_Videos')),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('WID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Well')),
            ],
        ),
        migrations.CreateModel(
            name='Yield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yield', models.FloatField(default=0.0)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('WID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Well')),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='HID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Household'),
        ),
        migrations.AddField(
            model_name='crop',
            name='FID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Farm'),
        ),
        migrations.AddField(
            model_name='crop',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Season'),
        ),
    ]
