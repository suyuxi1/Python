'''
excel基础写操作.py
@Author : su 
@Time   : 2020/04/20 23:13:49
'''

import xlsxwriter

#创建一个excel文件并作为当前工作簿
workbook = xlsxwriter.Workbook('./pythonLearn/excel/excel_demo1.xlsx')
# 添加一个工作表，默认名称是Sheet1，Sheet2等，可以指定名称
worksheet1 = workbook.add_format()
#指定名称：Data
worksheet2 = workbook.add_worksheet('Data')
#写数据
#向worksheet1 指定单元格写入内容
worksheet1.write('A1','Hello world')
#向worksheet2写入一组数据并用公式求和
expenses = (['Rent','2020-01-13',100000],
    ['Gas','2020-02-15',1024],
    ['Food','2020-02-16',14520],
    ['Gyn','2020-02-17',2036]
)
row = 0
col = 0
    # 遍历数据，用不同格式写入
for item ,cost in (expenses):
   worksheet2.write(row,col,item)
   worksheet2.write(row,col +1, cost)
   row +=1
# 写一个公式，计算出总和
worksheet2.write(row, 0, 'Total')
worksheet2.write(row,1 ,'=SUM(B1:B4)')
workbook.close()