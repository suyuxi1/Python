'''
列表切片.py
@Author : su 
@Time   : 2020/04/02 20:34:56
'''
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear','mangao']
#列表切片
fruits2 = fruits[1:4]
print(fruits2) #['apple', 'strawberry', 'waxberry']
fruits3 = fruits[:]
print(fruits3) 
#['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mangao']
fruits4 = fruits[-3:-1]
print(fruits4)
#['pitaya', 'pear']
#可以通过反向切片操作来获得倒转后的列表拷贝
fruits5 = fruits[::-1]
print(fruits5)
#['mangao', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']