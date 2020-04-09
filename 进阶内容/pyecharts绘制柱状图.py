'''
pyecharts绘制柱状图.py
@Author : su 
@Time   : 2020/04/09 23:24:45
'''

from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 内置主题类型可查看 pyecharts.globals.ThemeType
# 有LICHT DARK WHITE CHALK ESSOS INFOGRAPHIC
# MACAROUS PURPLE_PASSION ROMA ROMANTIC SHINE
# VINTAGE WALDEN WESTEROS WONDERLAND等十种

# 第一幅画，数据固定
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(['服饰', '箱包', '鞋帽', '电子', '数码', '户外'])
    .add_yaxis('京东',[5, 20, 36, 18, 78, 90])
    .add_yaxis('天猫',[5, 20, 36, 18, 78, 90])
    .set_global_opts(title_opts=opts.TitleOpts(title='电商销售对比'))
)
bar.render(path="./res/电商对比.html")


items = ['java', 'c', 'Pyhton', 'c++', 'JavaScript', 'c#', 'PHP', 'SQL']
data_list1 = [188, 166, 110, 108, 90, 80, 55, 45]
data_list2 = [190, 160, 140, 100, 80, 70, 50, 40]
bar1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(items)
    .add_yaxis("2020年", data_list1)
    .add_yaxis("2019年", data_list2)
    .set_global_opts(title_opts=opts.TitleOpts(title='编程预言排序', subtitle='2019-2020'))
)
bar.render(path="./res/编程语言排序.html")
