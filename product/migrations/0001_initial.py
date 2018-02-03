# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('value', models.DecimalField(verbose_name=b'Valor', max_digits=6, decimal_places=2)),
                ('bar_code', models.CharField(unique=True, max_length=13, verbose_name='C\xf3digo de Barras')),
            ],
        ),
    ]
