# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import lti_provider.field_validators


class Migration(migrations.Migration):

    dependencies = [
        ('lti_provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='key',
            field=models.CharField(max_length=128, unique=True, validators=[lti_provider.field_validators.validate_oauth_chars, lti_provider.field_validators.validate_oauth_length], verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='secret',
            field=models.CharField(max_length=128, unique=True, validators=[lti_provider.field_validators.validate_oauth_chars, lti_provider.field_validators.validate_oauth_length], verbose_name='Secret'),
        ),
    ]