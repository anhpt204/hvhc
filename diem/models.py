# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from daotao.models import DoiTuong, SinhVien, MonThi

from django.db import models

# Create your models here.
class LoaiDiem(models.Model):
    ten = models.CharField(max_length=50, unique=True, verbose_name="Loại điểm")
    viet_tat = models.CharField(max_length=20, verbose_name="Viết tắt")
    nhap_diem_theo_so_phach = models.BooleanField(default=True, verbose_name="Nhập điểm theo số phách")

    class Meta:
        verbose_name = verbose_name_plural = 'Loại điểm thi'

    def __unicode__(self):
        return u'%s' %self.ten

class TyLeDiem(models.Model):
    doi_tuong = models.ForeignKey(DoiTuong, verbose_name="Đối tượng")
    loai_diem = models.ForeignKey(LoaiDiem, verbose_name="Loại điểm")
    ty_le = models.FloatField(default=10, verbose_name="Tỷ lệ (%)")
    thu_tu_cham = models.PositiveIntegerField(verbose_name="Thứ tự nhập điểm", default=1, help_text='Thứ tự cho phép nhập điểm, nhập giá trị từ 1')

    class Meta:
        verbose_name = verbose_name_plural = "Tỷ lệ điểm"
        ordering = ['thu_tu_cham']


class KetQuaThi(models.Model):
    sinh_vien=models.ForeignKey(SinhVien,
                         blank=False, null=False,
                         verbose_name="Sinh viên")
    mon_thi = models.ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")

    loai_diem = models.ForeignKey(LoaiDiem, verbose_name='Loại điểm')

    diem = models.FloatField(default=0.0,
                              verbose_name="Điểm")
    class Meta:
        # unique_together = (('sinh_vien', 'mon_thi', 'loai_diem'),)
        verbose_name = "Điểm"
        verbose_name_plural = "Bảng điểm"
