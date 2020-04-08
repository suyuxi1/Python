'''
使用pycharts绘制仪表盘.py
@Author : su 
@Time   : 2020/04/08 23:57:59
'''
from pyecharts import charts

guage = charts.Gauge()
guage.add('python小列子',
          [('python机器学习', 30), ('python基础', 70), ('Python正则', 90)])
guage.render(path="./res/仪表盘.html")
print('ok')

