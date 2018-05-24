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
    return x

data = {}
for i in range(0, 16):
    d = readXL('Overload-Protection-new.xlsx', i)
    data[i] = d

print "Done Parsing"

for i in data:
    f = open('coloumn'+str(i)+'.txt', 'w')
    for j in data[i]:
        f.write('%s\n'%str(j))
    f.close()
    print i
