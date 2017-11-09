# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20150801_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdata',
            name='patient_image',
        ),
    ]
