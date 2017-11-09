# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_code', models.CharField(max_length=200)),
                ('physician_name', models.CharField(max_length=200)),
                ('patient_picture', models.ImageField(upload_to='uploads')),
            ],
        ),
    ]
