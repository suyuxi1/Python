'''
继承Thread类创建自定义的线程.py
@Author : su 
@Time   : 2020/04/11 22:37:24
'''

from time import time
from threading import Thread

import requests

# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('../res/img/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    # 使用了天行数据接口提供的网络API
    resp = requests.get('http://api.tianapi.com/allnews/index?key=df9e5d37918c5a819f8523e2efb1b36d&num=10&col=7')
    # 将服务器返回的JSON格式的数据解析为字典 
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()

if __name__ == "__main__":
    main()