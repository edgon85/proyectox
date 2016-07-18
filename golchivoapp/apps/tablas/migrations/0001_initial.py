# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField(default=1)),
                ('equipo', models.CharField(blank=True, max_length=120)),
                ('partidos', models.IntegerField(default=0)),
                ('goles', models.CharField(max_length=10)),
                ('diferencia', models.IntegerField(default=0)),
                ('puntos', models.IntegerField(default=0)),
            ],
        ),
    ]
