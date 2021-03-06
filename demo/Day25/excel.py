'''
excel.py
@Author : su 
@Time   : 2020/04/18 22:02:15
'''
import xlrd

# 1.打开工作簿
workbook = xlrd.open_workbook('./res/excel/班级卡片数据.xlsx')

# 2.工作表
# 输入所有sheet的名字
print(workbook.sheet_names())
# 获取所有的sheet
print(workbook.sheets())
# 根据索引获取sheet
print(workbook.sheet_by_index(0))
# 根据名字获取sheet
print(workbook.sheet_by_name('工作表1'))

# 3.行、列操作
sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)
# 获取第二行内容
print(sheet1.row_values(1))
# 获取第三列内容
print(sheet1.col_values(2))

# 4.单元格操作
cell1 = sheet1.cell(1,1).value
print(cell1)
cell2 = sheet1.cell(1)[1].value
print(cell2)
cell3 = sheet1.cell(1,2).value
print(cell3)
cell4 = sheet1.cell(2)[1].value
print(cell4)

# 5.日期类型（在对应的单元格准备好日期数据）
date_value = xlrd.xldate_as_datetime(
    sheet1.cell_value(1,2),workbook.datemode)
print(type(date_value), date_value)
