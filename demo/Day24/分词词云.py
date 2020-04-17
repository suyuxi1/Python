'''
分词词云.py
@Author : su 
@Time   : 2020/04/17 21:46:09
'''
import jieba
import wordcloud

# 构建并配置词云对象w
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#6c909e',
    colormap='GnBu',
    font_path='./res/font/SimHei.ttf'
)
# 调用jieba的Lcut()方法对原文件进行中文分词，得到string
txt = 'Spring 5是流行的Java应用程序开发框架的最新版本，该框架在Spring中引入了反应式编程特性。\
        毫无疑问，由于Spring是最流行的Java开发框架，因此有必要了解Spring 5中有哪些新特性，并使自己保持最新状态。\
        我个人喜欢食谱书，因为它们是基于任务的，这就是为什么我选择这本书和其他Spring 5书籍一起学习的原因。\
        它不仅涵盖了Spring 5的新特性，而且还涵盖了在早期版本上完成的所有其他增强功能。简而言之，它将教会您如何在Spring 5中编写代码。'
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('./res/img/output4.png')