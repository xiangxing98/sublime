README.md
# learn python3 

## Learn Python 3 Sample Code
thanks michaelliao
https://github.com/michaelliao/learn-python3

## learnpythonthehardway
http://learnpythonthehardway.org/
英文官网： http://learnpythonthehardway.org/book/ （第3版） 
中文纸书：http://www.queshu.com/book/35969824/ （第3版） 
中文html： http://sebug.net/paper/books/LearnPythonTheHardWay/（第2版） 
（有时加载很长时间页面还是空白，点地址栏旁边的X就出来了） 

## Python Resources

https://www.python.org/

http://www.w3cschool.cc/python/python-tutorial.html

http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html

http://www.douban.com/group/python/

http://www.baidu.com/s?wd=python&ie=UTF-8

## Python Resources
https://www.python.org/
https://wiki.python.org/moin/Python2orPython3

## Python Group
http://www.douban.com/group/python/

## Python快速教程
http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html

## Python入门教程 超详细1小时学会Python
http://www.jb51.net/article/926.htm

## Python 基础教程
http://www.runoob.com/python/python-tutorial.html

## liaoxuefeng Python 2.7教程
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/

## liaoxuefeng Python 3教程
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

## Baidu Python
http://www.baidu.com/baidu?wd=python&tn=monline_4_dg

```python
# Case-sensitive
a = 1
A = 2
print(a is not A)   # True

# Comments will be ignored

# Code blocks are defined by their indentation
# Use 4 spaces per indentation level.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Number
## integer
a = 1
b = 0x10            # 16
print(type(a))      # <class 'int'>

## float
c = 1.2
d = .5              # 0.5
g = .314e1          # 3.14
print(type(g))      # <class 'float'>

## complex
e = 1+2j
f = complex(1, 2)
print(type(e))      # <class 'complex'>
print(f == e)       # True

# String
s1 = '🐶\n'
s2 = "Dogge's home"
s3 = """
Hello,
Dogge!
"""
print(type(s1))     # <class 'str'>
print("%s, %s, %s" % (s1, s2, s3))
# 🐶
# , Dogge's home,
# Hello,
# Dogge!

## Length
print(len(s1))      # 2

## Slicing
s = '学而时习之'
print('{0}:{1}'.format(s[0], s[-2]))    # 学:习

# Byte
## 0-255/x00-xff
byt = b'abc'
print(type(byt))    # <class 'bytes'>
print(byt[0] == 'a')# False
print(byt[0] == 97) # True

## Length
print(len(byt))     # 3

# Boolean
True
False
print(type(True))   # <class 'bool'>

# None
print(None is None) # True
print(type(None))   # <class 'NoneType'>

# List
l = ['python', 3, 'in', 'one']
print(type(l))      # <class 'list'>

## Length
print(len(l))       # 4

## Slicing
print(l[0])         # 'python'
print(l[-1])        # 'one'
print(l[1:-1])      # [3, 'in']

## Alter
l.append('pic')     # None
# l == ['python', 3, 'in', 'one', 'pic']
l.insert(2, '.4.1') # None
# l == ['python', 3, '.4.1', 'in', 'one', 'pic']
l.extend(['!', '!'])
# l == ['python', 3, '.4.1', 'in', 'one', 'pic', '!', '!']


print(l.pop())             # '!'
# l == ['python', 3, '.4.1', 'in', 'one', 'pic', '!']
print(l.pop(2))           # '.4.1'
# l == ['python', 3, 'in', 'one', 'pic', '!']
l.remove("in")
# l == ['python', 3, 'one', 'pic', '!']
del l[2]
# l == ['python', 3, 'pic', '!']

print(l.index('pic'))       # 2

# Tuple
tp = (1, 2, 3, [4, 5])
print(type(tp)) # <class 'tuple'>

## Length
print(len(tp))  # 4

print(tp[2])    # 3
tp[3][1] = 6
print(tp)       # (1, 2, 3, [4, 6])

## Single element
tp = (1, )      # Not tp = (1)

## Assign multiple values at once
v = (3, 2, 'a')
(c, b, a) = v
print(a, b, c)  # a 2 3

# Set

# Dict
```

