'''
列表排序.py
@Author : su 
@Time   : 2020/04/02 20:24:41
'''
list1 = ['orange', 'apple', 'zoom', 'internationalization', 'blueberry']
list2 = sorted(list1)
#sorted函数返回列表排序后的拷贝不会修改传入列表
list3 = sorted(list1, reverse = True)
#通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted (list1, key = len)
print(list1)
print(list2)
print(list3)
print(list4)
#给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)