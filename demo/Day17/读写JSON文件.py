'''
读写JSON文件.py
@Author : su 
@Time   : 2020/04/11 22:10:16
'''

# json模块主要有四个比较重要的函数，分别是：
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成Python
# loads - 将字符串的内容反序列化成Python对象

import json

def main():
    # 定义字典对象
    mydict = {
        'name': 'Jack',
        'age': 20,
        'qq':123456,
        'friends': ['BOb', 'Mary'],
        'car': [
            {'brand': '奥迪', 'max-speed': 280},
            {'brand': '奔驰', 'max-speed': 320}
        ]
    }
    try:
        # 将字典对象序列化到文件中
        with open('./res/Jack.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

    try:
        # 从文件中读入，反序列化对象
        with open('./res/Jack.json', 'r', encoding='utf-8') as fs:
            mydict = json.load(fs)
            print(mydict)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('保存数据完成！')

if __name__ == "__main__":
    main()