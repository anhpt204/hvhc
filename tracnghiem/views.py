
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
    BaiThi
import json
from django.views.generic.detail import DetailView
from _io import BytesIO
from tracnghiem.util import export_pdf


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_user(request):
    logout(request)
    username = password = ''
    
#     ds_mothi = MonThi.objects.all();
    today = datetime.now().date()
    ds_cathi = KHThi.objects.filter(ngay_thi=today)
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
            
            baithi = BaiThi.objects.filter(thi_sinh=username, khthi=cathi_id)[0]
            return HttpResponseRedirect('/hvhc/tracnghiem/baithi/' + str(baithi.id) + '/')
         
    return HttpResponse(template.render(context))

def quiz_finish(request, pk):
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
    
#     user = request.user
#     user.logout()
    logout(request)
    
    return HttpResponse('Diem = ' + str(baithi.diem))

class BaiThiDetailView(DetailView):
    model = BaiThi
    template_name='baithi_detail.html'
#     pk_url_kwarg = 'cathi'
    
#     def get(self, request, *args, **kwargs):
#         return DetailView.get(self, request, *args, **kwargs)


class BaiThiStartView(DetailView):
    model = BaiThi
    template_name = 'baithi_start.html'
    
#     def get(self, request, *args, **kwargs):
#         object = DetailView.get(self, request, *args, **kwargs)
#         
#         context = self.get_context_data(object=self.object)
        
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        
                
        context['questions'] = self.object.get_ds_cauhoi()
        context['traloi'] = self.object.get_traloi().values()
        
        return context
    
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

def export_baithi_cauhoi(request, pk):
    baithi = BaiThi.objects.get(pk=pk)
    ds_cauhoi = baithi.get_ds_cauhoi()
         
    dethi = NganHangDe.objects.get(pk = baithi.khthi.de_thi_id)
    pdf = export_pdf(dethi, ds_cauhoi)
    
    file_name = str(baithi.thi_sinh.ma_sv) + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+file_name
     
 
    response.write(pdf)
    return response


def boc_tron_de_thi(request, pk):
    khthi = KHThi.objects.get(pk=pk)
    
    succ = khthi.boc_va_tron_de()
    if succ:
        return HttpResponse("Boc va tron de thanh cong!")
    else:
        return HttpResponse("Boc va tron de KHONG thanh cong!")
    
def khthi_show(request, pk):
    khthi = KHThi.objects.get(pk=pk)
    ds_baithi = khthi.get_ds_baithi()
    
    template = loader.get_template('ds_thisinh.html')
    context = RequestContext(request, {
        'khthi':khthi,
        'ds_baithi': ds_baithi,
    })
    
    return HttpResponse(template.render(context))