# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20170110_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='image',
            field=models.ForeignKey(default=b'0', to='mainapp.Image'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='user',
            field=models.ForeignKey(default=b'0', to='mainapp.User'),
        ),
    ]
