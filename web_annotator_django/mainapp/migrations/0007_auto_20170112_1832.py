# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20170110_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='image',
        ),
        migrations.AddField(
            model_name='page',
            name='image_src',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
