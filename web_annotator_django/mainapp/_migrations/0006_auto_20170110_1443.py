# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20170110_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manuscript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MSCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('manuscript', models.ForeignKey(to='mainapp.Manuscript')),
            ],
        ),
        migrations.AddField(
            model_name='manuscript',
            name='collection',
            field=models.ForeignKey(to='mainapp.MSCollection'),
        ),
    ]
