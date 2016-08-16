# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from common.models import KHThiBase
from daotao.models import SinhVien
from diem.models import LoaiDiem, TyLeDiem
from chamthi import *

# Create your models here.
class NhapDiem(models.Model):
    khthi = models.ForeignKey(KHThiBase, verbose_name=u'Ca thi')
    # trang_thai =  models.CharField(max_length=30, choices=TT_CHAMTHI, default=TT_CHAMTHI_CHUACODIEM, verbose_name='Trạng thái')
    diem_can_cham = models.ForeignKey(TyLeDiem, verbose_name="Điểm cần nhập")

    class Meta:
        verbose_name = verbose_name_plural = 'Nhập điểm sinh viên'

        permissions = (
            (PERM_NHAP_DIEM_DOC_DUONG, 'Người dùng được phép nhập điểm dọc đường'),
            (PERM_NHAP_DIEM_1, 'Cho phép giáo viên chấm thi 1 nhập điểm'),
            (PERM_NHAP_DIEM_2, 'Cho phép giáo viên chấm thi 2 nhập điểm'),
            (PERM_NHAP_DIEM_3, 'Cho phép giáo viên chấm thi 3 nhập điểm'),
            )


    def __unicode__(self):
        return u'%s' %self.khthi.ten

    # override a save function, to make diem cho tung sv (ChamDiemSV)
    def save(self, *args, **kwargs):
        # get loai diem cho doi tuong
        ty_le_diems = TyLeDiem.objects.filter(doi_tuong=self.khthi.doi_tuong)
        for sv in self.khthi.ds_thisinh.all():
            for ty_le_diem in ty_le_diems:

                cham_diem = ChamDiemSV()
                cham_diem.nhap_diem = self
                cham_diem.sinh_vien = sv
                cham_diem.loai_diem = ty_le_diem.loai_diem
                cham_diem.diem = 0.0

                cham_diem.save()

        super(NhapDiem, self).save(*args, **kwargs)

class ChamDiemSV(models.Model):
    nhap_diem = models.ForeignKey(NhapDiem)
    sinh_vien = models.ForeignKey(SinhVien, verbose_name='Sinh viên')
    loai_diem = models.ForeignKey(LoaiDiem, verbose_name='Loại điểm')
    diem = models.FloatField(default=0.0, verbose_name='Điểm')

    class Meta:
        verbose_name = verbose_name_plural = 'Điểm sinh viên'

    def __unicode__(self):
        return u'%s' %self.nhap_diem.khthi.ten
