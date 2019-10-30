# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from utils.load_data import load_data


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0004_remove_exporttype_model'),
    ]

    operations = [
        migrations.RunPython(
            load_data('export/migrations/data/bl_alpha_solrmarc_02.json',
                      'default')),
    ]