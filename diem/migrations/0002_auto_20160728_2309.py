# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 23:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tylediem',
            old_name='diem',
            new_name='loai_diem',
        ),
        migrations.AlterField(
            model_name='loaidiem',
            name='ten',
            field=models.CharField(max_length=50, unique=True, verbose_name='Lo\u1ea1i \u0111i\u1ec3m'),
        ),
        migrations.AlterField(
            model_name='tylediem',
            name='doi_tuong',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='daotao.DoiTuong', verbose_name='\u0110\u1ed1i t\u01b0\u1ee3ng'),
        ),
    ]