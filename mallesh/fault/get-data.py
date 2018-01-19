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

ax = plt.gca()

data1 = readXL('fault.xlsx', 2)
data2 = readXL('fault.xlsx', 4)

data1 = range(1, 101)
data2 = []

data1 = readXL('fault.xlsx', 5)
data2 = readXL('fault.xlsx', 7)

tfile = open('flood.txt', 'w')

for i, j in zip(data1, data2):
    tfile.write('%s\t'%(i))
    tfile.write('%s\n'%(j))

tfile.close()

