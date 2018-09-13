import xlrd
import numpy as np

def readXL(f, col):
    x = []
    workbook = xlrd.open_workbook(f)
    sheet = workbook.sheet_by_name('Sheet1')
    for value in sheet.col_values(col):
        if isinstance(value, float):
            x.append(value)
        else:
            x.append(0)
    return x

data1 = readXL('fault_tolerance_stateless.xlsx', 1)
data2 = readXL('fault_tolerance_stateless.xlsx', 0)

tfile = open('sl_nf_data.txt', 'w')

for i, j in zip(data1, data2):
    tfile.write('%s\t'%(i))
    tfile.write('%s\n'%(j))

tfile.close()


