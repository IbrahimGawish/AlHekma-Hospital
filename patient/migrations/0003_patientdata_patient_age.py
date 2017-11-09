# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patientdata_diagnostics'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdata',
            name='patient_age',
            field=models.IntegerField(default=0),
        ),
    ]
