'''
@Author  : su 
@File    : 字符串常用方法练习.py
@Time    : 2020/03/31 22:45:53
'''
def main():
    str1 = 'hello, world!'
    # 通过内置函数len计算字符串的长度
    print(len(str1))#13
    #获得字符串首字母的戏字母的拷贝
    print(str1.capitalize())
    # 获得字符串每个单词首字母的戏字母的拷贝
    print(str1.title())
    #获得字符串变大写后的拷贝
    print(str1.upper())
    #从字符串中查找字串所在的位置
    print(str1.find('or'))
    #检查字符串是否以指定的字符串开头
    print(str1.startswith('he'))
    print(str1.startswith('hel'))
    #检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))
    #将字符串以指定的宽度居中开头并在两侧填充指定的字符
    print(str1.center(50,"*"))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50,' '))
    str2 = 'abcd123456'
    #检查字符串是否有数据构成1q
    print(str2.isdigit())
    #检查字符串是否以字母构成
    print(str2.isalpha())
    #检查字符串是否以数字和字母构成
    print(str2.isalnum())
    str3 = 'hello@126.com'
    print(str3)
    #获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())

if __name__ =='__main__':
    main()