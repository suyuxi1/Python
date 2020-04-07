'''
元组类型练习.py
@Author : su 
@Time   : 2020/04/07 20:34:41
'''

#定义元组
t = ('张晨', 18, True, '江苏南京')
print(t)
#获取元组中的元素
print(t[0])
print(t[3])
#遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤' # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '广东广州')
print(t)
# 将元组装换成列表
person = list(t)
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)