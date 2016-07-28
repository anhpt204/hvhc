# -*- encoding: utf-8 -*-
# default_app_config = "tracnghiem.apps.QuizConfig"
# from hrm.models import *
# from daotao.models import *
# from tracnghiem import models as tracnghiemmodels


TFQUESTION='TF'
MCQUESTION='MC'
ESSAYQUESTION='ESSAY'

HK1 = 'HK1'
HK2 = 'HK2'

KHTHI_CHUATHI = 'CHUA_THI'
KHTHI_DANGTHI = 'DANG_THI'
KHTHI_DATHI = 'DA_THI'

PERM_BOC_DE = 'duoc_phep_boc_de'
PERM_XEM_IN_DE = 'duoc_phep_xem_va_in_de'

QUESTION_TYPES=(
               (TFQUESTION, 'Câu hỏi Đúng - Sai'),
               (MCQUESTION, 'Câu hỏi Multiple Choice'),
               (ESSAYQUESTION, 'Câu hỏi tự luận'),
               )

TRANG_THAI_THI=(
                ('DA_THI', 'Đã thi'),
                ('VANG_CO_LD', 'Vắng có lý do'),
                ('VANG_KO_LD', 'Vắng không lý do'),
                )
TRANG_THAI_KHTHI=(
                (KHTHI_CHUATHI, 'Chưa thi'),
                (KHTHI_DANGTHI, 'Đang thi'),
                (KHTHI_DATHI, 'Đã thi'),
                )

ANSWER_ORDER_OPTIONS = (
    ('CONTENT', 'Nội dung'),
    ('RANDOM', 'Ngẫu nhiên'),
    ('NONE', 'None')
)

HOC_KY = (
          (HK1, 'Học kỳ 1'),
          (HK2, 'Học kỳ 2')
          )

# lam tron diem
DIEM_LAMTRON1 = 'Lam tron cach 1'
DIEM_LAMTRON2 = 'Lam tron cach 2'

DIEM_LAMTRON = (
    (DIEM_LAMTRON1, 'Cách 1'),
    (DIEM_LAMTRON2, 'Cách 2'),
)
