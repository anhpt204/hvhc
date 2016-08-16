# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-28 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('daotao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KetQuaThi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diem', models.FloatField(default=0.0, verbose_name='\u0110i\u1ec3m')),
            ],
            options={
                'verbose_name': '\u0110i\u1ec3m',
                'verbose_name_plural': 'B\u1ea3ng \u0111i\u1ec3m',
            },
        ),
        migrations.CreateModel(
            name='LoaiDiem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, verbose_name='Lo\u1ea1i \u0111i\u1ec3m')),
                ('viet_tat', models.CharField(max_length=20, verbose_name='Vi\u1ebft t\u1eaft')),
            ],
            options={
                'verbose_name': 'Lo\u1ea1i \u0111i\u1ec3m thi',
                'verbose_name_plural': 'Lo\u1ea1i \u0111i\u1ec3m thi',
            },
        ),
        migrations.CreateModel(
            name='TyLeDiem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ty_le', models.FloatField(default=10, verbose_name='T\u1ef7 l\u1ec7 (%)')),
                ('diem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diem.LoaiDiem', verbose_name='Lo\u1ea1i \u0111i\u1ec3m')),
                ('doi_tuong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daotao.DoiTuong', verbose_name='\u0110\u1ed1i t\u01b0\u1ee3ng')),
            ],
            options={
                'verbose_name': 'T\u1ef7 l\u1ec7 \u0111i\u1ec3m',
                'verbose_name_plural': 'T\u1ef7 l\u1ec7 \u0111i\u1ec3m',
            },
        ),
        migrations.AddField(
            model_name='ketquathi',
            name='loai_diem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diem.LoaiDiem', verbose_name='Lo\u1ea1i \u0111i\u1ec3m'),
        ),
        migrations.AddField(
            model_name='ketquathi',
            name='mon_thi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daotao.MonThi', verbose_name='M\xf4n thi'),
        ),
        migrations.AddField(
            model_name='ketquathi',
            name='sinh_vien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daotao.SinhVien', verbose_name='Sinh vi\xean'),
        ),
        migrations.AlterUniqueTogether(
            name='ketquathi',
            unique_together=set([('sinh_vien', 'mon_thi', 'loai_diem')]),
        ),
    ]
