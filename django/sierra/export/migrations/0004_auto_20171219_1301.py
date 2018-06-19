# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from utils.load_data import load_data


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0003_auto_20171219_1255'),
    ]

    operations = [
        migrations.RunPython(
            load_data('export/migrations/data/blacklight_dev01_export.json',
                      'default')),
    ]