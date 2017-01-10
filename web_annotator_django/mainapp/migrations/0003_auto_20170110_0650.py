# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('src', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='src',
        ),
        migrations.AddField(
            model_name='annotation',
            name='user',
            field=models.ForeignKey(default=0, to='mainapp.User'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='image',
            field=models.ForeignKey(default=0, to='mainapp.Image'),
        ),
    ]
