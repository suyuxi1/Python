'''
爬取实验楼所有课程信息.py
@Author : su 
@Time   : 2020/04/14 22:00:25
'''

import requests
from lxml import html

def crawl():
    course_list = []
    for num in range(1, 25):
        url = 'https://www.shiyanlou.com/courses/page=' + str(num)
        content = requests.get(url)
        tree = html.fromstring(content.text)
        course_name = tree.xpath('//h6[@class="course-name"]/text()')
        course_descriptions = tree.xpath('//div[@class="course_description"]/text()')
        course_covers = tree.xpath('//img[@class="cover-image"]/@src')
        for index in range(0, len(course_name)-1):
            temp_dict = {}
            temp_dict['name'] = course_name[index].strip()
            temp_dict['description'] = course_descriptions[index].strip()
            temp_dict['cover'] = course_covers[index]
            course_list.append(temp_dict)
            print(len(course_list))
    return course_list

if __name__ == "__main__":
    list = crawl()
    print(len(list))
