'''
pyhton数据分组.py
@Author : su 
@Time   : 2020/04/09 23:12:25
'''

from itertools import groupby
weather = [{'date': '2019-12-15', 'weather': 'cloud'},
           {'date': '2019-12-13', 'weather': 'sunny'},
           {'date': '2019-12-14', 'weather': 'cloud'}]
# 分组前没有安装分组字段排序，分组失败
for k, items in groupby(weather, key=lambda x: x['weather']):
    print(k)
    for i in items:
        print(i)
print('********************************')

# 分组前按照分组字段排序，分组成功
weather.sort(key=lambda x: x['weather'])
for k, items in groupby(weather, key=lambda x: x['weather']):
    print(k)
    for i in items:
        print(i)