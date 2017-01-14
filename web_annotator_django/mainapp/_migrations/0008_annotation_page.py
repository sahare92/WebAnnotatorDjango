# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20170112_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='page',
            field=models.ForeignKey(default='', to='mainapp.Page'),
            preserve_default=False,
        ),
    ]
