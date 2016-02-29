# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idComp', models.IntegerField(unique=True, blank=True, null=True)),
                ('nameComp', models.CharField(blank=True, max_length=150, null=True)),
                ('ipAdress', models.CharField(blank=True, max_length=16, null=True)),
                ('netmask', models.CharField(blank=True, max_length=16, null=True)),
                ('compState', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idusr', models.CharField(blank=True, max_length=120, null=True)),
                ('pwdusr', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
