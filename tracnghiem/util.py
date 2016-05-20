# -*- coding: utf-8 -*-
'''
Created on Dec 24, 2015

@author: pta
'''
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import black
from _io import BytesIO
from hvhc import settings
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from os.path import join
from django.utils import timezone
# PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]

pdfmetrics.registerFont(TTFont('Times', join(settings.BASE_DIR, 'static/fonts/times.ttf')))
pdfmetrics.registerFont(TTFont('TimesBd', join(settings.BASE_DIR, 'static/fonts/timesbd.ttf')))
pdfmetrics.registerFont(TTFont('TimesIt', join(settings.BASE_DIR, 'static/fonts/timesi.ttf')))
pdfmetrics.registerFont(TTFont('TimesBI', join(settings.BASE_DIR, 'static/fonts/timesbi.ttf')))

styles = getSampleStyleSheet()
PAGE_WIDTH, PAGE_HEIGHT = A4
print PAGE_WIDTH, PAGE_HEIGHT, inch, PAGE_WIDTH/inch, PAGE_HEIGHT/inch


question_style= ParagraphStyle(
            'my_par_style',
            fontName='TimesBd',
            fontSize=13,
            leading=18,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            alignment=TA_JUSTIFY,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Times',
            bulletFontSize=13,
            bulletIndent=1,
            textColor= black,
            backColor=None,
            wordWrap=None,
            borderWidth= 0,
            borderPadding= 0,
            borderColor= None,
            borderRadius= None,
            allowWidows= 1,
            allowOrphans= 0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        )

answer_stype = ParagraphStyle(
            'my_par_style',
            fontName='Times',
            fontSize=13,
            leading=18,
            leftIndent=20,
            rightIndent=0,
            firstLineIndent=20,
            alignment=TA_JUSTIFY,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Times',
            bulletFontSize=13,
            bulletIndent=1,
            textColor= black,
            backColor=None,
            wordWrap=None,
            borderWidth= 0,
            borderPadding= 0,
            borderColor= None,
            borderRadius= None,
            allowWidows= 1,
            allowOrphans= 0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        )

pageinfo = "platypus example"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('TimesBd',13)
#     canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-80, Title)

    canvas.setFont('Times',13)
    canvas.drawString(PAGE_WIDTH/2.0, 0.75 * inch, "%d" % doc.page)
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times',13)
    canvas.drawString(PAGE_WIDTH/2.0, 0.75 * inch, "%d" % (doc.page))
    canvas.restoreState()


def export_pdf(de_thi, dapan):
    '''
    export de thi trac nghiem ra pdf
    '''
    socau = len(dapan)
    table_data=[]
    table_data.append([u'HỌC VIỆN HẬU CẦN', u'ĐỀ THI KẾT THÚC MÔN'])
    table_data.append([u'%s' %de_thi.logSinhDe.monHoc.khoa.ten_dv, u'MÔN: ' + de_thi.logSinhDe.monHoc.ten_mon_thi])
    table_data.append([u'', u'Đối tượng: ' + de_thi.logSinhDe.doiTuong.ten_dt])
    table_data.append([u'', u'Thời gian: '])
    table_data.append([u'', u'Đề gồm: ' + str(socau) + u' câu'])

    buf = BytesIO()

#     file_name = 'dethi.pdf'
    doc = SimpleDocTemplate(buf)
    pars = [Spacer(1, 0.1*inch)]
#     pars = []
    title_table = Table(table_data, colWidths=[(PAGE_WIDTH-100)/2.0]*2)
    title_table.setStyle(TableStyle([('FONT', (0,0), (1,1), 'TimesBd', 13),
                                     ('FONT', (0,2), (-1,-1), 'Times', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ]))
    pars.append(title_table)

    pars.append(Spacer(1, 0.5*inch))

    sv_info_table_data = [[u'Mã môn học: '+ de_thi.logSinhDe.monHoc.ma_mon_thi + u'     - Số tín chỉ (hoặc đvht):    ' , u'Mã đề thi']]
    sv_info_table_data.append([u'Lớp: ' ,de_thi.maDeThi])
    sv_info_table_data.append([u'Mã học viên, sinh viên: ',''])
    sv_info_table_data.append([u'Họ tên học viên, sinh viên: ',''])

    sv_info_table = Table(sv_info_table_data, colWidths=[PAGE_WIDTH-200, 100])
    sv_info_table.setStyle(TableStyle([('FONT', (1,0), (-1,-1), 'TimesBd', 13),
                                       ('FONT', (0,0), (0,-1), 'Times', 13),
                                      ('ALIGN', (1,0), (-1,-1), 'CENTER'),
                                      ('BOX', (1,0), (-1,-1), 1.25, colors.black),
                                      ]))
    pars.append(sv_info_table)
    pars.append(Spacer(1, 0.5*inch))


    n = 1
    for question, answers in dapan:
        # question
        p = Paragraph(u'Câu ' + str(n) + ": " + question.noiDung, question_style)
        n += 1
        pars.append(p)
        # answers
        ls = ['A. ', 'B. ', 'C. ', 'D. ']
        for l, answer in zip(ls, answers):
            pars.append(Spacer(1, 0.03*inch))
            p = Paragraph(l + answer.dapAn, answer_stype)
            pars.append(p)
            pars.append(Spacer(1, 0.03*inch))

        pars.append(Spacer(1, 0.05*inch))

    # ký
    sig_table_data = [[u'-------HẾT--------', u'']]
    sig_table_data.append([u'' ,u'TRƯỞNG KHOA'])
    sig_table_data.append([u'' ,u'(Ký, họ tên)'])

    sig_table = Table(sig_table_data, colWidths=[PAGE_WIDTH-300, 200])
    sig_table.setStyle(TableStyle([('FONT', (0,0), (1,0), 'Times', 13),
                                       ('FONT', (0,1), (1,1), 'TimesBd', 13),
                                       ('FONT', (0,2), (1,2), 'TimesIt', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ('SPAN',(0,0),(1,0)),
                                      ]))
    pars.append(sig_table)

    doc.build(pars, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buf.getvalue()
    buf.close()
    return pdf

def export_baithi_pdf(de_thi, dapan, baithi):
    '''
    export de thi trac nghiem ra pdf
    '''
    socau = len(dapan)
    table_data=[]
    table_data.append([u'HỌC VIỆN HẬU CẦN', u'ĐỀ THI KẾT THÚC MÔN'])
    table_data.append([u'%s' %de_thi.logSinhDe.monHoc.khoa.ten_dv, u'MÔN: ' + de_thi.logSinhDe.monHoc.ten_mon_thi])
    table_data.append([u'', u'Đối tượng: ' + de_thi.logSinhDe.doiTuong.ten_dt])
    table_data.append([u'', u'Thời gian: '])
    table_data.append([u'', u'Đề gồm: ' + str(socau) + u' câu'])

    buf = BytesIO()

#     file_name = 'dethi.pdf'
    doc = SimpleDocTemplate(buf)
    pars = [Spacer(1, 0.1*inch)]
#     pars = []
    title_table = Table(table_data, colWidths=[(PAGE_WIDTH-100)/2.0]*2)
    title_table.setStyle(TableStyle([('FONT', (0,0), (1,1), 'TimesBd', 13),
                                     ('FONT', (0,2), (-1,-1), 'Times', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ]))
    pars.append(title_table)

    pars.append(Spacer(1, 0.5*inch))

    sv_info_table_data = [[u'Mã môn học: '+ de_thi.logSinhDe.monHoc.ma_mon_thi + u'     - Số tín chỉ (hoặc đvht):    ' , u'Mã đề thi']]
    sv_info_table_data.append([u'Lớp: ' ,de_thi.maDeThi + baithi.thi_sinh.ma_sv.split('-')[1]])
    sv_info_table_data.append([u'Mã học viên, sinh viên: ',''])
    sv_info_table_data.append([u'Họ tên học viên, sinh viên: ',''])

    sv_info_table = Table(sv_info_table_data, colWidths=[PAGE_WIDTH-200, 100])
    sv_info_table.setStyle(TableStyle([('FONT', (1,0), (-1,-1), 'TimesBd', 13),
                                       ('FONT', (0,0), (0,-1), 'Times', 13),
                                      ('ALIGN', (1,0), (-1,-1), 'CENTER'),
                                      ('BOX', (1,0), (-1,-1), 1.25, colors.black),
                                      ]))
    pars.append(sv_info_table)
    pars.append(Spacer(1, 0.5*inch))


    n = 1
    for question, answers in dapan:
        # question
        p = Paragraph(u'Câu ' + str(n) + ": " + question.noiDung, question_style)
        n += 1
        pars.append(p)
        # answers
        ls = ['A. ', 'B. ', 'C. ', 'D. ']
        for l, answer in zip(ls, answers):
            pars.append(Spacer(1, 0.03*inch))
            p = Paragraph(l + answer.dapAn, answer_stype)
            pars.append(p)
            pars.append(Spacer(1, 0.03*inch))

        pars.append(Spacer(1, 0.05*inch))

    # ký
    sig_table_data = [[u'-------HẾT--------', u'']]
    sig_table_data.append([u'' ,u'TRƯỞNG KHOA'])
    sig_table_data.append([u'' ,u'(Ký, họ tên)'])

    sig_table = Table(sig_table_data, colWidths=[PAGE_WIDTH-300, 200])
    sig_table.setStyle(TableStyle([('FONT', (0,0), (1,0), 'Times', 13),
                                       ('FONT', (0,1), (1,1), 'TimesBd', 13),
                                       ('FONT', (0,2), (1,2), 'TimesIt', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ('SPAN',(0,0),(1,0)),
                                      ]))
    pars.append(sig_table)

    doc.build(pars, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buf.getvalue()
    buf.close()
    return pdf

def export_baithi_dapan_pdf(de_thi, dapan, baithi):
    '''
    export de thi trac nghiem ra pdf
    '''
    socau = len(dapan)
    table_data=[]
    table_data.append([u'HỌC VIỆN HẬU CẦN', u'ĐÁP ÁN MÔN THI'])
    table_data.append([u'%s' %de_thi.logSinhDe.monHoc.khoa.ten_dv, u'MÔN: ' + de_thi.logSinhDe.monHoc.ten_mon_thi])
    table_data.append([u'', u'Đối tượng: ' + de_thi.logSinhDe.doiTuong.ten_dt])
    table_data.append([u'', u'Thời gian: '])
    table_data.append([u'', u'Đề gồm: ' + str(socau) + u' câu'])

    buf = BytesIO()

#     file_name = 'dethi.pdf'
    doc = SimpleDocTemplate(buf)
    pars = [Spacer(1, 0.1*inch)]
#     pars = []
    title_table = Table(table_data, colWidths=[(PAGE_WIDTH-100)/2.0]*2)
    title_table.setStyle(TableStyle([('FONT', (0,0), (1,1), 'TimesBd', 13),
                                     ('FONT', (0,2), (-1,-1), 'Times', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ]))
    pars.append(title_table)

    pars.append(Spacer(1, 0.5*inch))

    sv_info_table_data = [[u'Mã môn học: '+ de_thi.logSinhDe.monHoc.ma_mon_thi + u'     - Số tín chỉ (hoặc đvht):    ' , u'Mã đề thi']]
    sv_info_table_data.append([u'Lớp: ' ,de_thi.maDeThi + baithi.thi_sinh.ma_sv.split('-')[1]])
    sv_info_table_data.append([u'Mã học viên, sinh viên: ',''])
    sv_info_table_data.append([u'Họ tên học viên, sinh viên: ',''])

    sv_info_table = Table(sv_info_table_data, colWidths=[PAGE_WIDTH-200, 100])
    sv_info_table.setStyle(TableStyle([('FONT', (1,0), (-1,-1), 'TimesBd', 13),
                                       ('FONT', (0,0), (0,-1), 'Times', 13),
                                      ('ALIGN', (1,0), (-1,-1), 'CENTER'),
                                      ('BOX', (1,0), (-1,-1), 1.25, colors.black),
                                      ]))
    pars.append(sv_info_table)
    pars.append(Spacer(1, 0.5*inch))

    for i in xrange(1, len(dapan)+1):
        cau_hoi = str(i)
        dap_an = dapan[cau_hoi]
        # question
        p = Paragraph(u'Câu ' + cau_hoi + ": " + dap_an, answer_stype)
        pars.append(p)
        pars.append(Spacer(1, 0.05*inch))

    # ký
    sig_table_data = [[u'-------HẾT--------', u'']]
    sig_table_data.append([u'' ,u'TRƯỞNG KHOA'])
    sig_table_data.append([u'' ,u'(Ký, họ tên)'])

    sig_table = Table(sig_table_data, colWidths=[PAGE_WIDTH-300, 200])
    sig_table.setStyle(TableStyle([('FONT', (0,0), (1,0), 'Times', 13),
                                       ('FONT', (0,1), (1,1), 'TimesBd', 13),
                                       ('FONT', (0,2), (1,2), 'TimesIt', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ('SPAN',(0,0),(1,0)),
                                      ]))
    pars.append(sig_table)

    doc.build(pars, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buf.getvalue()
    buf.close()
    return pdf

def export_bangdiem(baithi):
    '''
    export bang diem ra pdf
    '''
    rows_len = len(baithi)
    table_data=[]
    table_data.append([u'BỘ QUỐC PHÒNG', u'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM'])
    table_data.append([u'HỌC VIỆN HẬU CẦN', u'Độc lập - Tự do - Hạnh phúc'])
    table_data.append([u'', u'Hà Nội, ngày ' + str(timezone.now().day) + u' tháng ' + str(timezone.now().month) + u' năm ' + str(timezone.now().year)])

    buf = BytesIO()

#     file_name = 'dethi.pdf'
    doc = SimpleDocTemplate(buf)
    pars = [Spacer(1, 0.1*inch)]
#     pars = []
    title_table = Table(table_data, colWidths=[250, PAGE_WIDTH-250])
    title_table.setStyle(TableStyle([('FONT', (0,0), (1,1), 'TimesBd', 13),
                                     ('FONT', (0,2), (-1,-1), 'Times', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ]))
    pars.append(title_table)

    pars.append(Spacer(1, 0.5*inch))

    bd_title_table_data = [[u'BÁO CÁO KẾT QUẢ THI']]
    bd_title_table_data.append([u'môn: ' + baithi[0].khthi.mon_thi.ten_mon_thi + u'     đvht: ' + str(baithi[0].khthi.mon_thi.so_dvht)])

    ngay_thi = '%d - %d - %d' %(baithi[0].khthi.ngay_thi.day, baithi[0].khthi.ngay_thi.month, baithi[0].khthi.ngay_thi.year)
    bd_title_table_data.append([u'lớp: ' + baithi[0].thi_sinh.lop.ten_lop + u'      ngày thi: ' + ngay_thi])

    bd_title_table = Table(bd_title_table_data, colWidths=[PAGE_WIDTH])
    bd_title_table.setStyle(TableStyle([('FONT', (0,0), (0,0), 'TimesBd', 14),
                                       ('FONT', (0,1), (-1,-1), 'Times', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      #('BOX', (1,0), (-1,-1), 1.25, colors.black),
                                      ]))
    pars.append(bd_title_table)
    pars.append(Spacer(1, 0.5*inch))

    bd_table_data = [[u'STT', u'Họ tên', u'Điểm', u'Ghi chú']]
    n = 1
    for bt in baithi:
	row = [str(n), bt.thi_sinh.get_ho_ten, str(bt.diem), ""]
	bd_table_data.append(row)
	n = n + 1

    bd_table = Table(bd_table_data, colWidths=[50, 250, 50, 100])
    bd_table.setStyle(TableStyle([('FONT', (0,0), (3,0), 'TimesBd', 13),
                                       ('FONT', (0,1), (-1,-1), 'Times', 13),
                                      ('ALIGN', (0,0), (-1,0), 'CENTER'), #header
                                      ('ALIGN', (0,0), (0,-1), 'CENTER'), #STT
				      ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                      ('BOX', (0,0), (-1,-1), 0.5, colors.black),
                                      ]))
    pars.append(bd_table)
    pars.append(Spacer(1, 0.5*inch))


    # ký
    sig_table_data = [[u'-------HẾT--------', u'']]
    sig_table_data.append([u'' ,u'TRƯỞNG KHOA'])
    sig_table_data.append([u'' ,u'(Ký, họ tên)'])

    sig_table = Table(sig_table_data, colWidths=[PAGE_WIDTH-300, 200])
    sig_table.setStyle(TableStyle([('FONT', (0,0), (1,0), 'Times', 13),
                                       ('FONT', (0,1), (1,1), 'TimesBd', 13),
                                       ('FONT', (0,2), (1,2), 'TimesIt', 13),
                                      ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                      ('SPAN',(0,0),(1,0)),
                                      ]))
    pars.append(sig_table)

    doc.build(pars, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buf.getvalue()
    buf.close()
    return pdf

if __name__ == '__main__':
    pass
