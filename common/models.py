# -*- encoding: utf-8 -*-

'''
Created on Sep 18, 2015

@author: pta
'''
from django.db import models
from daotao.models import DoiTuong, MonThi, SinhVien
from hrm.models import GiaoVien
from hvhc import PERM_BOC_DE, PERM_XEM_IN_DE, HOC_KY, HK1, HK2
from django.utils import timezone

class KHThiBase(models.Model):
    '''
    Thiet lap mot ca thi, trong do co danh sach cau hoi de tu do lam
    cac de thi cho tung sinh vien
    '''
    ten = models.CharField(verbose_name=u"Tên", max_length=200, blank=False)

    nam_hoc = models.CharField(max_length=9,
                        verbose_name=u"Năm học",
                        help_text=u"Nhập năm học theo định dạng XXXX-XXXX. Ví dụ 2015-2016")

    hoc_ky = models.CharField(max_length=3,
                              choices=HOC_KY,
                            default=HK1,
                            verbose_name=u"Học kỳ")

    doi_tuong = models.ForeignKey(DoiTuong,
                           verbose_name=u"Đối tượng")

    mon_thi = models.ForeignKey(MonThi, blank=False, null=False,
                         related_name='%(class)s_monthi_cathi',
                         verbose_name="Môn thi")

    ds_giamthi = models.ManyToManyField(GiaoVien, related_name='%(class)s_giamthi_khthi',
                                 verbose_name=u'Danh sách giám thị coi thi')

    ds_thisinh = models.ManyToManyField(SinhVien, blank=False, related_name='%(class)s_sinhvien_khthi',
                                verbose_name=u'Danh sách thí sinh')
#     ds_thisinh.help_text = u'Tìm kiếm theo họ tên sinh viên hoặc mã lớp.'

    ngay_thi = models.DateField(verbose_name="Ngày thi", default=timezone.now)
    tg_bat_dau=models.TimeField(verbose_name="Thời gian bắt đầu", default=timezone.now)
#     tg_ket_thuc=TimeField(verbose_name="Thời gian kết thúc")
    tg_thi = models.PositiveIntegerField(verbose_name="Thời gian thi (phút)", default=30, help_text="Nhập thời gian thi tính bằng đơn vị phút")

    nguoi_boc_de = models.ForeignKey(GiaoVien, verbose_name="Người bốc đề", null=True, blank=True)

    class Meta:
        verbose_name = u"Kế hoạch thi - bốc đề"
        verbose_name_plural = u"Kế hoạch thi - bốc đề"
        permissions = ((PERM_BOC_DE, 'Người dùng được phép bốc đề'),
                        (PERM_XEM_IN_DE, 'Người dùng được phép xem và in đề'),)

    def __unicode__(self):
        return u'%s' %(self.ten)
