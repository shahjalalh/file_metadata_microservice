# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-16 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile', models.FileField(upload_to=b'')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
