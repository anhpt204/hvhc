# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('tracnghiem', '0011_auto_20151226_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedUser',
            fields=[
                ('user', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
