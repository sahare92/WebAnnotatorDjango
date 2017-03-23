# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20170110_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='image',
            field=models.ForeignKey(to='mainapp.Image'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='user',
            field=models.ForeignKey(to='mainapp.User'),
        ),
    ]
