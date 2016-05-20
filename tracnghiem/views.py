# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template import loader
from django.views.decorators.csrf import csrf_protect

from datetime import datetime
from tracnghiem.models import LogSinhDe, NganHangDe, Question, Answer, KHThi,\
    BaiThi, LoggedUser, ImportMCQuestion
import json
from django.views.generic.detail import DetailView
from _io import BytesIO
from tracnghiem.util import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from hvhc import KHTHI_DANGTHI, KHTHI_CHUATHI, KHTHI_DATHI
from hrm.models import GiaoVien


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def user_login(request):
    if request.user:
        logout(request)
    username = password = ''

#     ds_mothi = MonThi.objects.all();

    ds_cathi = KHThi.objects.filter(ngay_thi=timezone.now).exclude(trang_thai__exact=KHTHI_DATHI)
#     ds_cathi = KHThi.objects.all()


    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'ds_cathi': ds_cathi,
    })

    if(request.POST):
        username = request.POST['username']
        password = request.POST['password']
        cathi_id = request.POST['cathi']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if username.startswith('GV'):
                khthi = KHThi.objects.get(pk=cathi_id)
                if not khthi:
                    return HttpResponse('<h1>Tên đăng nhập hoặc mật khẩu sai. Bấm <a href=\"/hvhc/tracnghiem/\">VÀO ĐÂY</a> để đăng nhập lại</h1>')
                ds_giamthi = khthi.ds_giamthi.all()
                for giamthi in ds_giamthi:
                    if giamthi.user.id == user.id:
                        return HttpResponseRedirect('/hvhc/tracnghiem/khthi/theodoithi/'+str(khthi.id) + '/')
            else:
                ds_baithi = BaiThi.objects.filter(thi_sinh=username, khthi=cathi_id)
                if not ds_baithi:
                    return HttpResponse('<h1>Tên đăng nhập hoặc mật khẩu sai. Bấm <a href=\"/hvhc/tracnghiem/\">VÀO ĐÂY</a> để đăng nhập lại</h1>')

                baithi = ds_baithi[0]
                if baithi.khthi.trang_thai==KHTHI_DATHI or baithi.is_finished:
                    return HttpResponse('<center><h1>Bài thi đã hoàn thành! Điểm bài thi này là: %.1f</h1></center>' %baithi.diem)
                else:
                    return HttpResponseRedirect('/hvhc/tracnghiem/baithi/' + str(baithi.id) + '/')

    return HttpResponse(template.render(context))

def theodoithi(request, pk):
    khthi = KHThi.objects.get(pk=pk)
    ds_thisinh = khthi.ds_thisinh.all()
    login_users = LoggedUser.objects.all()

#     print login_users

    ds_thisinh_info = []
    for thisinh in ds_thisinh:
        logged_in, login_time = check_login_user(thisinh, login_users)
        ds_thisinh_info.append([thisinh, logged_in, login_time])

    print ds_thisinh_info

    template = loader.get_template('theodoithi.html')
    context = RequestContext(request, {
        'khthi': khthi,
        'ds_thisinh': ds_thisinh_info,
        'khthi_chuathi':KHTHI_CHUATHI,
        'khthi_dangthi':KHTHI_DANGTHI
    })
    return HttpResponse(template.render(context))

def theodoithi_batdau(request, pk):
    khthi = KHThi.objects.get(pk=pk)
    khthi.trang_thai = KHTHI_DANGTHI
    khthi.tg_thi_batdau = timezone.now().time()
    khthi.save()

    ds_thisinh = khthi.ds_thisinh.all()
    login_users = LoggedUser.objects.all()

#     print login_users

    ds_thisinh_info = []
    for thisinh in ds_thisinh:
        logged_in, login_time = check_login_user(thisinh, login_users)
        ds_thisinh_info.append([thisinh, logged_in, login_time])

#     print ds_thisinh_info

    template = loader.get_template('theodoithi.html')
    context = RequestContext(request, {
        'khthi': khthi,
        'ds_thisinh': ds_thisinh_info,
        'khthi_chuathi':KHTHI_CHUATHI,
        'khthi_dangthi':KHTHI_DANGTHI
    })
    return HttpResponse(template.render(context))

def theodoithi_ketthuc(request, pk):
    khthi = KHThi.objects.get(pk=pk)
    khthi.trang_thai = KHTHI_DATHI
    khthi.save()
    logout(request)

    return HttpResponse('Bạn đã thoát khỏi hệ thống. Bấm <a href=\'/hvhc/tracnghiem/ \'> VÀO ĐÂY </a> để đăng nhập lại')


def check_login_user(thisinh, loggedin_users):
    for u in loggedin_users:
#         print thisinh.ma_sv, u.username, u.login_time
        if thisinh.user.username == u.username.strip():
#             print 'OK'
            return True, u.login_time
    return False, None

def baithi_finish(request, pk):
    if not request.user.is_authenticated():
        return  HttpResponseRedirect('/hvhc/tracnghiem/')

    baithi = BaiThi.objects.get(pk=pk)

    answers = {}

    if request.POST:
        questions = json.loads(baithi.ds_cauhoi)
        for q_id,_ in questions:
            try:
                answers[q_id] = int(request.POST[q_id])
            except:
                continue

    baithi.save_tralois(answers)

    baithi.cham_diem()
    baithi.finish()

    logout(request)
    template = loader.get_template('ketqua.html')
    context = RequestContext(request, {
        'diem': baithi.diem,
    })
    return HttpResponse(template.render(context))

def baithi_save(request, pk, cau):
    if not request.user.is_authenticated():
        return  HttpResponseRedirect('/hvhc/tracnghiem/')

    baithi = BaiThi.objects.get(pk=pk)

    answers = {}

    if request.POST:
        questions = json.loads(baithi.ds_cauhoi)
        for q_id,_ in questions:
            try:
                answers[q_id] = int(request.POST[q_id])
            except:
                continue

    baithi.save_tralois(answers)

    return HttpResponseRedirect('/hvhc/tracnghiem/baithi/' + str(baithi.pk) + '/start/#cau_'+str(cau))

class BaiThiDetailView(DetailView):
    model = BaiThi
    template_name='baithi_detail.html'
#     pk_url_kwarg = 'cathi'

#     def get(self, request, *args, **kwargs):
#         return DetailView.get(self, request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)


        context['khthi'] = self.object.khthi
        context['thi_sinh'] = self.object.thi_sinh
        context['khthi_dangthi'] = KHTHI_DANGTHI

        return context
# @login_required
class BaiThiStartView(DetailView):
    model = BaiThi
    template_name = 'baithi_start.html'

#     def get(self, request, *args, **kwargs):
#         object = DetailView.get(self, request, *args, **kwargs)
#
#         context = self.get_context_data(object=self.object)
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        # get remaining time
        dathi_duration = timezone.now().hour*60 + timezone.now().minute
        dathi_duration = dathi_duration - (self.object.khthi.tg_thi_batdau.hour*60 + self.object.khthi.tg_thi_batdau.minute)
        remaining_time = self.object.khthi.tg_thi - dathi_duration

        context['questions'] = self.object.get_ds_cauhoi()
        context['traloi'] = self.object.get_traloi().values()
        context['socaudatraloi'] = len(self.object.get_traloi())
        context['soluongcauhoi'] = len(self.object.get_ds_cauhoi())
        context['remaining_time'] = remaining_time
        return context
@login_required
def start_baithi(request, pk):
    baithi = BaiThi.objects.get(pk=pk)
    if baithi.khthi.trang_thai != KHTHI_DANGTHI:
        return HttpResponseRedirect('/hvhc/tracnghiem/baithi/' + str(pk) + '/')

    template = loader.get_template('baithi_start.html')

    dathi_duration = timezone.now().hour*60 + timezone.now().minute
    dathi_duration = dathi_duration - baithi.khthi.tg_thi_batdau.hour*60 + baithi.khthi.tg_thi_batdau.minute
    remaining_time = baithi.khthi.tg_thi - dathi_duration

    context = RequestContext(request, {
        'baithi':baithi,
#         'questions':baithi.get_ds_cauhoi(),
#         'traloi': baithi.get_traloi().values(),
#         'socaudatraloi': len(baithi.get_traloi()),
#         'soluongcauhoi':len(baithi.get_ds_cauhoi()),
#         'remaining_time': remaining_time
    })
    return template.render(context)

def sinhde(request, pk):
    logSinhDe = LogSinhDe.objects.get(pk=pk)
    ok, msg = logSinhDe.sinhDe()

    # if ok then render to a new page that list all generated dethi
    return HttpResponse(msg)

def export(request, pk):
    dethi = NganHangDe.objects.get(pk=pk)
    dapan = []
    id_cauhois = dethi.questions.split(',')
    for id_cauhoi in id_cauhois:
        cauhoi = Question.objects.get(pk = id_cauhoi)
        answers = Answer.objects.filter(question=cauhoi)
        dapan.append([cauhoi, answers])

    pdf = export_pdf(dethi, dapan)

    file_name = dethi.maDeThi + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+file_name


    response.write(pdf)
    return response

def export_bd(request, bts):
    ids = bts.split('-')
    ids = [int(i) for i in ids]
    baithis = []
    for bt_id in ids:
	baithi = BaiThi.objects.get(pk=bt_id)
	baithis.append(baithi)

    pdf = export_bangdiem(baithis)

    file_name = 'bangdiem.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+file_name


    response.write(pdf)
    return response

#    return HttpResponse(bts)


def export_baithi_cauhoi(request, pk):
    baithi = BaiThi.objects.get(pk=pk)
    ds_cauhoi = baithi.get_ds_cauhoi()

    dethi = NganHangDe.objects.get(pk = baithi.khthi.de_thi_id)
    pdf = export_baithi_pdf(dethi, ds_cauhoi, baithi)

    file_name = str(baithi.thi_sinh.ma_sv) + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+file_name


    response.write(pdf)
    return response


def export_baithi_dapan(request, pk):
    baithi = BaiThi.objects.get(pk=pk)
    dapan = baithi.get_dapan()

    dethi = NganHangDe.objects.get(pk = baithi.khthi.de_thi_id)
    pdf = export_baithi_dapan_pdf(dethi, dapan, baithi)

    file_name = str(baithi.thi_sinh.ma_sv) + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+file_name


    response.write(pdf)
    return response


def boc_tron_de_thi(request, pk):
    khthi = KHThi.objects.get(pk=pk)
    # get nguoi boc de
    nguoi_boc_de = GiaoVien.objects.get(user__pk = request.user.pk)

    succ = khthi.boc_va_tron_de(nguoi_boc_de)
    logout(request)
    if succ:
#         return HttpResponseRedirect("/hvhc/tracnghiem/khthi/show/" + str(pk) + "/" )
        return HttpResponse("Bốc và trộn đề thành công! Bấm <a href=\"/admin\">VÀO ĐÂY</a> để đăng nhập lại vào hệ thống.")
    else:
        return HttpResponse(u"Bốc và trộn đề thi KHÔNG thành công! Kiểm tra lại cấu hình sinh đề thi.")

def khthi_show(request, pk):
    khthi = KHThi.objects.get(pk=pk)
    ds_baithi = khthi.get_ds_baithi()

    template = loader.get_template('ds_thisinh.html')
    context = RequestContext(request, {
        'khthi':khthi,
        'ds_baithi': ds_baithi,
    })

    return HttpResponse(template.render(context))


def import_mcquestion(request, pk):
    import_mcq = ImportMCQuestion.objects.get(pk=pk)
    import_mcq.import_data()
    return HttpResponse('<h1>Đã cập nhật dữ liệu xong!</h1>')
