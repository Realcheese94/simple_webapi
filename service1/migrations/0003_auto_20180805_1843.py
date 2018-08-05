# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-05 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service1', '0002_personinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=10)),
                ('animal_size', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='personinfo',
            name='person_no',
        ),
        migrations.DeleteModel(
            name='PersonInfo',
        ),
    ]
