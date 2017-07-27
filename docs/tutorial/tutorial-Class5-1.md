---
title: 文件读写
codes: {"exmple code":"/tutorial/demo5-1.py",
"result":"/tutorial/demo5-1.csv"}
---

本文详细内容可以参考[官方文档](http://python.usyiyi.cn/documents/python_352/library/index.html)中查询或者到[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000)。

# 文件操作与文件流
在之前的所有代码中，我们的输入设备都是键盘，而输出设备都是显示器。

但是，在实际应用环境中，我们有时需要把结果保存下来，或者从一个已有的结果进一步计算。

这时，我们就会要用到文件操作。

## 打开文件
`open(file,mode='r',encoding=None,errors=None)`

在Python中，提供了一个内置函数`open()`可以用来访问操作系统所提供的文件API接口，`open()`函数返回一个文件对象，我们可以通过该文件对象来访问文件流中的数据。

关于`open()`函数的完整信息可以参考[官方文档](http://python.usyiyi.cn/documents/python_352/library/functions.html#open)。

### 参数 file
此参数表示文件URL，可以是绝对路径或相对路径，如`'D:/VS/test.txt'` `./a.csv`

### 参数 mode
此参数是指明文件打开的模式，常用的几个模式如下:
>`open()`函数默认的打开模式为`rt`.

字符 | 含义
-----|----------
 'r' | 读取模式
 'w' | 写入模式 
 'a' | 追加模式
 't' | 文本模式
 'b' | 二进制模式

### 参数 encoding
此参数是指明用于文件的编码格式，只能用于文本模式下

### 参数 errors
参函数是指明如何处理编码和解码错误

* `ignore`：忽略错误
* `replace`：替代所选字符所在的错误位置

### 文件读写
在Python中，文件对象已经自带了`read()`和`write()`方法，我们可以很方便的对文件进行读写操作。
> 当然还有`readline()`,`writeline()`等方法

### 关闭文件
在我们对一个文件执行完操作之后，我们必须释放该文件，不然会导致其他程序无法访问。

在Python中，我们可以使用`f.close()`来关闭一个文件对象。

## 文件流
保存在磁盘上的文件中数据被定义为文件流。

其实我们最熟悉的`print()`和`input()`所指向的也是两个文件流，分别为标准输出流和标准输入流。

# 上下文管理
python提供`with`方法，该方法允许自定义用户类去定义在语句体执行前进入并且在语句结束时退出的运行时上下文。

* `with open() as f`:
在Python中，已经实现了`open()`函数的上下文管理，`with open() as f`我们可以用这种形式来简化我们对文件对象的管理。

>利用内置函数`open()`方法打开文件时，每次打开之后，最后都要调用`close()`方法关闭文件，而且如果打开的文件不存在，就会因为无法`close()`而抛出异常，所以python提供了`with open() as f`发放自动调用`close()` 

# csv
csv是最常用的电子表格和数据库的导出导入格式，详细信息请参考[官方文档](http://python.usyiyi.cn/documents/python_352/library/csv.html)。

所在，在Python标准库中，也提供了相应的库来简化对CSV文件的操作。

## csv.writer
示例代码

```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
```
注意：
>这一有一个`newline`参数，如果没有`newline=''`，写入的数据每行之间都会有空行，也就是说`newline`的默认参数为换行符

## csv.reader
示例代码

```python
import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
