'''
Created on Sep 18, 2015

@author: pta
'''
from tuluan.models import DeThi, KHThiTuLuan, BoDe
from os.path import basename, join
from django.http import HttpResponse
import os
from django.views.generic.detail import DetailView
import random
from django.http.response import HttpResponseRedirect
from hvhc.settings import BASE_DIR


def print_dt(request, pk):
    dt = DeThi.objects.get(pk=pk)
    if dt:
        file_name = basename(dt.de_thi.path)
        pdf = open(dt.de_thi.path, 'rb').read()
#         pdf = PyPDF2.PdfFileReader(open(dt.de_thi.path, 'rb'))
        response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'inline; filename=%s' %(file_name)
#         return response
        return response
    else:
        return HttpResponse(u'No file')

def view_pdf(request, pk):
    dt = DeThi.objects.get(pk=pk)
    if dt:
        file_name = basename(dt.de_thi.path)
        pdf = open(dt.de_thi.path, 'r').read()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=%s' %(file_name)
        return response
    else:
        return HttpResponse(u'No file %s' %(file_name))

def view_dethi(request, pk):
    dt = DeThi.objects.get(pk=pk)
    if dt:
        file_name = basename(dt.de_thi.path)
        pdf = open(join(BASE_DIR, dt.de_thi.path), 'r').read()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=%s' %(file_name)
        return response
    else:
        return HttpResponse(u'No file %s' %(file_name))

def view_dapan(request, pk):
    dt = DeThi.objects.get(pk=pk)
    if dt:
        file_name = basename(dt.dap_an.path)
        pdf = open(join(BASE_DIR, dt.dap_an.path), 'r').read()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=%s' %(file_name)
        return response
    else:
        return HttpResponse(u'No file %s' %(file_name))


class CaThiView(DetailView):
    model = KHThiTuLuan
    template_name='sinhde_tuluan.html'

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        # lay ngan hang de thi tuong ung voi doi_tuong va mon_thi
        ngan_hang = BoDe.objects.filter(doi_tuong=self.object.doi_tuong,
                                                        mon_thi=self.object.mon_thi)

        context['ds_bo_de'] = ngan_hang

        return context

#     def get_context_data(self, **kwargs):
#         context = DetailView.get_context_data(self, **kwargs)
#         # neu da co de roi, thi khong sinh de moi nua
#         dethi_tmp = self.object.ds_de_thi.all()
#         if dethi_tmp and len(dethi_tmp)==self.object.so_de_thi:
#             context['ds_de_thi'] = self.object.ds_de_thi.all()
#             return context
#         # lay tat ca ca thi cua cua hoc ky, cung doi tuong va mon thi
#         same_cathi = CaThiTuLuan.objects.filter(nam_hoc=self.object.nam_hoc,
#                                                 hoc_ky=self.object.hoc_ky,
#                                                 doi_tuong=self.object.doi_tuong,
#                                                 mon_thi=self.object.mon_thi)
#         de_da_thi = set()
#         for ct in same_cathi:
#             if ct != self.object:
#                 de_da_thi.update(set(ct.ds_de_thi.all()))
#
#         # lay ngan hang de thi tuong ung voi doi_tuong va mon_thi
#         ngan_hang = NganHangDeThiTuLuan.objects.filter(doi_tuong=self.object.doi_tuong,
#                                                           mon_thi=self.object.mon_thi)
#
#         ngan_hang_dt = DeThiTuLuan.objects.filter(ngan_hang=ngan_hang[0])
#         # tao danh sach de chua thi
#         de_chua_thi = set(ngan_hang_dt).difference(de_da_thi)
#         # lay so_de_thi
#         de_thi_s = random.sample(de_chua_thi, self.object.so_de_thi)
#
#         for de_thi in de_thi_s:
#             self.object.ds_de_thi.add(de_thi)
#
#         self.object.save()
#
#         context['ds_de_thi'] = de_thi_s
#
#         return context

def sinh_de(request, pk):
    # get ca thi
    cathi_tuluan = KHThiTuLuan.objects.get(pk=pk)
    dethi_s = []
    # get bo de
    if request.POST:
        id_bode = int(request.POST['bo_de'])

        bo_de = BoDe.objects.get(pk=id_bode)
        # get de thi cua bo de
        ds_de_thi = DeThi.objects.filter(ngan_hang=bo_de)

        #sinh de
        dethi_s = random.sample(ds_de_thi, cathi_tuluan.so_de_thi)

        cathi_tuluan.ds_de_thi.clear()

        for dt in dethi_s:
            cathi_tuluan.ds_de_thi.add(dt)

        cathi_tuluan.save()

        return HttpResponseRedirect('/hvhc/tuluan/get_dt/%s/' %(pk))
