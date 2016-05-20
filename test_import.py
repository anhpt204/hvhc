'''
Created on Jan 14, 2016

@author: pta
'''

from openpyxl import load_workbook

wb = load_workbook('/home/pta/git/hvhc/media/tmp/de_trac_nghiem_TH.xls.xlsx')
ws = wb.active
# print len(ws.columns)
# print len(ws.rows)

t = 0
for row in ws.rows[1:]:
    if row[0].value == None:
        break
    print row[0].value
    t += 1
    
print t
    


