'''
对字符串进行32位加密.py
@Author : su 
@Time   : 2020/04/07 20:30:43
'''
import hashlib
#对字符串s实现32位加密

def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('UTF-8')))
    return m.hexdigest()

print(hash_cry32(1))
print(hash_cry32('hello'))