'''
外交文本词云.py
@Author : su 
@Time   : 2020/04/17 21:40:43
'''
import wordcloud
import random

# 读入外部文本文件
f = open('./res/test.txt', encoding='utf-8')
txt = f.read()
# 更换背景色和整体风格
w = wordcloud.WordCloud(
    scale=2,
    max_font_size=100,
    background_color='#383838',
    colormap='PuRd',
    font_path='./res/font/SimHei.ttf'
)
# 将txt变量传入
w.generate(txt)
w.to_file('./res/img/output3.png')