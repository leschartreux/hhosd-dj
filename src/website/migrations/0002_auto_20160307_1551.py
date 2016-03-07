# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('mac', models.CharField(null=True, db_column='MAC', blank=True, max_length=17)),
                ('ip', models.CharField(null=True, db_column='IP', blank=True, max_length=15)),
                ('nom', models.CharField(db_column='NOM', max_length=32)),
                ('salle', models.IntegerField(db_column='SALLE')),
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('type_connect', models.IntegerField(null=True, blank=True)),
                ('type_os', models.IntegerField(null=True, blank=True)),
                ('vm_audio', models.IntegerField(null=True, db_column='vm_audio', blank=True)),
                ('type_poste', models.CharField(null=True, db_column='TYPE_POSTE', blank=True, max_length=5)),
                ('login', models.CharField(null=True, blank=True, max_length=64)),
                ('pyddlaj', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'MACHINE',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Computer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
