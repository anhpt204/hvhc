# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daotao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ma_sv', models.PositiveIntegerField(unique=True, verbose_name=b'M\xc3\xa3 sinh vi\xc3\xaan')),
                ('ho_ten', models.CharField(max_length=50, verbose_name=b'H\xe1\xbb\x8d v\xc3\xa0 t\xc3\xaan')),
                ('lop', models.ForeignKey(verbose_name=b'L\xe1\xbb\x9bp', to='daotao.Lop')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sinh vi\xean',
                'verbose_name_plural': 'Danh s\xe1ch sinh vi\xean',
            },
        ),
        migrations.AddField(
            model_name='monthi',
            name='so_dvht',
            field=models.PositiveIntegerField(default=3, verbose_name=b'S\xe1\xbb\x91 \xc4\x91\xc6\xa1n v\xe1\xbb\x8b h\xe1\xbb\x8dc tr\xc3\xacnh'),
        ),
        migrations.AlterField(
            model_name='diem',
            name='sinh_vien',
            field=models.ForeignKey(verbose_name=b'Sinh vi\xc3\xaan', to='daotao.SinhVien'),
        ),
    ]
