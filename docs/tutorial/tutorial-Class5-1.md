---
title: 文件读写
codes: {"exmple code":"/tutorial/demo5-1.py",
"result":"/tutorial/demo5-1.csv"}
---

本文详细内容可以到[官方文档](http://python.usyiyi.cn/documents/python_352/library/index.html)中查询或者到[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000)自学

# 文件流
* 键盘和鼠标是特殊的文件流

# 打开文件
* `f = open(file,mode='r',encoding=None,errors=None)`

通常用上述`open()`方法打开文件
open()具体具体使用方式可到[官方文档](http://python.usyiyi.cn/documents/python_352/library/functions.html#open)中查询

## 参数 file
此参数表示文件名称，可以是当前目录的路径，如`(D://VS//test.txt)`

## 参数 mode
此参数是指明文件打开的模式，常用的几个模式如下
字符 | 含义
---------|----------
 'r' | 打开阅读(默认) 
 'w' | 打开写入 
 't' | 文本模式(默认)

## 参数 encoding
此参数是指明用于解码或编码文件的编码名称，只能用于文本模式下

## 参数 errors
参函数是指明如何处理编码和解码错误

* `ignore`：忽略错误
* `replace`：替代所选字符所在的错误位置

# 上下文管理
python提供`with`方法，该方法允许自定义用户类去定义在语句体执行前进入并且在语句结束时退出的运行时上下文。

* with open() as f:
利用内置函数`open()`方法打开文件时，每次打开之后，最后都要调用`close()`方法关闭文件，而且如果打开的文件不存在，就会因为无法`close()`而抛出异常，所以python提供了`with open() as f`发放自动调用`close()` 

# csv
csv是最常用的电子表格和数据库的导出导入格式，详细信息请到[官方文档](http://python.usyiyi.cn/documents/python_352/library/csv.html)查询

## csv.writer
示例代码
```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
```
注意：
* 这一有一个`newline`参数，如果没有`newline=''`，写入的数据每行之间都会有空行，也就是说`newline`的默认参数为换行符
## csv.reader
示例代码
```python
import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
