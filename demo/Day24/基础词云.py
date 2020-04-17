'''
基础词云.py
@Author : su 
@Time   : 2020/04/17 21:32:03
'''
import wordcloud
import random

# 创建词云对象
w = wordcloud.WordCloud()
# 通过字符串生成词云
w.generate('Coding is easier said than done, and there is a huge difference between good code and bad code, \
            but how do you know? Until you have seen a good code and know why a particular code is good, \
            you can not understand the difference.')
# 生成本地文件
w.to_file('./res/img/output1.png')

# 创建词云对象，设置词云图片宽、高、字体、背景色
# 中文字体需要提前下载中文字体文件
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eeeeee',
                        font_path='./res/font/SimHei.ttf')
w.generate('编码说起来容易做起来难，好的代码和坏的代码之间有巨大的区别，可是你怎么知道？\
            除非看到了好的代码并知道为什么很好，否则你无法理解它们之间的区别。')
w.to_file('./res/img/output2.png')