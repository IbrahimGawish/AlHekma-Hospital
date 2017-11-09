# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patientdata_patient_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdata',
            name='patient_image',
            field=models.CharField(max_length=200, default='h'),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='patient_picture',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
