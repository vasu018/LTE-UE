import random
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

data1 = readXL('TAUvsMig.xlsx', 6)
data2 = readXL('TAUvsMig.xlsx', 7)

tfile1 = open('sl_InterHostFT.txt', 'w')
tfile2 = open('sl_IntraHostFT.txt', 'w')

for i, j in zip(data1):
    tfile1.write('%s\t'%(i))

for i, j in zip(data2):
    tfile2.write('%s\t'%(i))
d1 = []
d2 = []
c = 88
for i in range(1000):
    c += 0.01
    tfile.write('%s\t'%(c)) 
    tfile.write('%s\n'%(random.random()*10))

tfile.close()

