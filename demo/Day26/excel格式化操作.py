'''
excel格式化操作.py
@Author : su 
@Time   : 2020/04/19 20:01:57
'''
from datetime import datetime
import xlsxwriter


def set_format():
    workbook = xlsxwriter.Workbook('./pythonLearn/res/excel/excel_demo.xlsx')
    worksheet = workbook.add_worksheet()
    #基础格式
    fmt = workbook.add_format({"font_name": u"微软雅黑", 'font-size':10})
    # 背景格式：定义字体，对齐方式，背景前景色等：
    bg_format = workbook.add_format({'bold':True,'font_name':u'微软雅黑','bg_color':'#217346',
    'align':'center','valign':'vcenter','font_color':'#282c34',
    'font_size':11,'border':1})
    #金额格式
    money_format = workbook.add_format({'num_format':'$#,##0'})
    #日期格式
    date_format = workbook.add_format({'num_format':'yyyy-mm-dd'})
    #设置行高，从第零行开始，行高设为20，格式为fmt
    worksheet.set_row(0,20,fmt)
    #设置列宽，从A列到C列，列宽为20，格式为fmt
    worksheet.set_colum('A:C',20,fmt)
    #用指定背景格式写入表头
    worksheet.write('A1','Item',bg_format)
    worksheet.write('B1','Date',bg_format)
    worksheet.write('C1','Cost',bg_format)

    expenses = (['Rent','2020-01-13',100000],
    ['Gas','2020-02-15',1024],
    ['Food','2020-02-16',14520],
    ['Gyn','2020-02-17',2036])
    row = 1
    col = 0
    # 遍历数据，用不同格式写入
    for item ,date_str, cost in (expenses):
        date = datetime.strftime(date_str, "%Y-%m-%d")
        worksheet.write_string(row,col,item)
        worksheet.write_datetime(row,col+1,date,date_format)
        worksheet.write_number(row,col+2,cost,money_format)
        row +=1
    worksheet.write(row,1,'Total')
    workbook.write(row,2,'=SUM(C2:C5)',money_format)
if __name__ == "__main__":
   set_format()