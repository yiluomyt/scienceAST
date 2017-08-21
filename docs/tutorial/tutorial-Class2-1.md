---
title: Python 基础
author: Ricardo
---

本篇内容参考自以下网站:
* [菜鸟教程](https://www.runoob.com/python/python-tutorial.html)
* [廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
* [Python 3.5.2官方文档](http://python.usyiyi.cn/translate/python_352/library/index.html)

更多信息可自行查阅。

# 基础数据类型
## number(数值)
python中数字类型分为三种：整型、浮点型和复数.
>复数的实部与虚部都是浮点型

Operation        | Result 
-----------------|----------
 `x + y`         | x 和 y 的和
 `x - y`         | x 和 y 的差
 `x * y`         | x 和 y 的积
 `x / y`         | x 和 y 的商
 `x // y`        | x 和 y 的商向下取整的整数
 `x % y`         | 对 x 求 y 的余数
 `-x`            | x 取负
 `abs(x)`        | x 的绝对值
 `int(x)`        | x 转换为整数
 `float(x)`      | x 转化为浮点数
 `c.conjugate()` | 复数c 的共轭
 `pow(x, y)`     | x的y次幂
 `x ** y`        | x的y次幂 

 完整文章请参阅[官方文档](http://python.usyiyi.cn/translate/python_352/library/stdtypes.html#numeric-types-int-float-complex)。

需要注意的是：
1. 浮点数在计算机中的储存是有精度限制的，所以可能发生四舍五入的情况。
1. 数值类型是为值类型，改变值后将返回一个新的对象。
    >关于值类型和引用类型的区别会在后文详细介绍

## str(字符串)
<!--TODO: 介绍一下切片的用法-->
关于python字符串的使用，可参考[菜鸟教程](http://www.runoob.com/python/python-strings.html)。

## bool(布尔值)
布尔是整数的一个子类型,它的返回值为True或者False.

下面是布尔运算:
1. `x or  y` => 一者真即为真
1. `x and y` => 一者假即为假
1. `not x  ` => 真为假，假为真

备注：
1. `and` 与 `or` 均为短路运算符,若第一个元素已经满足运算符的判断条件，则不会进行第二个运算符的计算。
1. `not` 是一个低优先级的布尔运算符，所以 `not a == b` 解释为 `not (a == b)`，且 `a == not b` 是一个语法错误。

## object
Python中所有变量都是对象,所有对象都基于`object`类(除元类以外).

# 基础数据结构
Python常用的数据结构有:
* `list`
* `tuple`
* `dict`
* `set`

为下文叙述方便，这里先提示一下，上述的4种数据结构对象，均为可迭代对象(`iterable`)

## list
`list`是一个可变的有序列表，可以通过索引访问到元素
1. 索引从0开始累计
1. `list`中的元素不需要具有相同的类型
1. 可以使用语法糖`[]`快速构建一个`list`

``` Python
# 使用默认构造函数创建一个list
list1 = list()
# 使用构造函数创建一个list,items是一个可迭代对象
(iterable)
list2 = list(items)
# 使用语法糖构建一个空列表
list3 = []
# 使用语法糖构建一个非空列表
# 元素间以`,`隔开
list4 = [False, 10, '20']
# 使用索引获取元素
# 因为索引从0开始累计，此处item值为10
item = list4[1]
```

`list`的更多使用方法可以参考[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)。


## tuple
`tuple`是一种不可变有序列表(语法糖为`()`)。`tuple`和`list`非常相似，但`tuple`在初始化之后就不可以修改。当然也就没有`append()`、`insert()`这样的方法。
>更进一步说，`tuple`的不可变是指`tuple`中所存元素的对象引用不可变。
* 对于值类型来说，对象引用不可变即代表值不可变。
* 但对于引用类型来说，引用类型的值可以在保持对象引用不变的情况下改变。

一个“可变”`tuple`的例子:
``` Python
tuple1 = (1, 2, [3])
print("Before: ", tuple1)
tuple1[2][0] = 4
print("After : ", tuple1)

# Result
# Before:  (1, 2, [3])
# After :  (1, 2, [4])
```

同时再补充一点关于`list`和`tuple`的区别：
* `list` 为可变序列，不可hash
* `tuple` 为不可变序列，可以[hash](https://baike.baidu.com/item/Hash/390310?fr=aladdin)

**注意**:
``` Python
# 在创建单元素tuple时，不可以写作(item)
# 注意此处()为理解为运算符()
# 所以a最后的类型为int, 值为1
a = (1)
# 若想用语法糖创建单元素tuple
# 可以通过添加`,`来消除歧义
# 此处b被正确的创建为tuple
b = (1,)
```

## dict
`dict`表示一种映射(mapping)关系，可以将hashable的值映射到任意对象。
* `dict`的语法糖形式表现为`{key1: value1, key2: value2, ...}`，其中key必须要为hashable对象。
* `dict`的查找速度为O(1),即查找速度不受包含元素个数影响。
    >相对的，`list`的查找速度为O(n),即查找速度与包含元素成线性相关。
* `dict`相对于`list`占用更多的内存。

``` Python
# 使用默认构造函数创建一个dict
d1 = dict()
# 创建一个空dict
d2 = {}
# 创建一个非空的dict
d3 = {'A':1, 'B':'2', 'C':[3]}
# 通过key取出所对应的value
print(d3['B'])
# 若key不存在，则会抛出一个KeyError
# print(d3['b'])
# 使用in运算符判断是否存在一个key
print('A' in d3) # True
print('D' in d3) # False
# 可以通过dict的get方法，来避免出现KeyError的情况
# 返回默认值None
print(d3.get('b'))
# 也可以自定义默认值
# 此处返回默认值0
print(d3.get('b', 0))
```

## set
`set`相当于不保存value的`dict`,因为key不可重复，所以`set`也可以理解为数学意义上的集合。
* `set`的语法糖形式表现为`{key1, key2, ...}`,其中key必须为hashable对象。
    >**注意**：`{}`创建的是一个空`dict`对象，若想创建一个空`set`对象，必须调用默认的无参构造函数`set()`
* `set`对象中的重复元素将被自动过滤。
* `set`对象可以执行数学意义上的交(并)集操作。

``` Python
# 仅可以使用默认的无参构造函数创建空set
s1 = set()
# 使用构造函数创建非空set
s2 = set([1, 2, 3])
# 创建非空set
# 过滤重复元素，即s3为{3, 4, 5}
s3 = {3, 4, 4, 5}
# 执行交集操作
print(s2 & s3) # {3}
# 执行并集操作
print(s2 | s3) # {1, 2, 3, 4, 5}
```

# 控制语句
## 条件语句(if...elif...else)
关于`if`条件语句可以参考[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000)。

注意：
1. 使用`if`语句时不能忘记`:`。
1. `if`语句是遵循自上而下判断，即如果`if`条件成立，后面的`elif`判断语句将被忽略。
1. `if`语句与代码块间有4个空格的缩进关系。

## 循环语句(for/while)
关于循环语句可以参考[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431676242561226b32a9ec624505bb8f723d0027b3e7000)。

注意：
* 无限循环时是`while True:` 而不是`while 1:`
* 在测试过程中，若出现代码死循环可以使用`ctrl+c`强制结束程序。

# 函数与成员访问
## 函数
关于函数调用可以参考[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167832686474803d3d2b7d4d6499cfd093dc47efcd000)。

常用的内建函数请参考[官方文档](http://python.usyiyi.cn/translate/python_352/library/functions.html)。

例如以下代码：
```python
def sum(a,b):
    return a+b
```
其中`def`是定义函数的关键字，`sum`是函数名，`a,b`是这个函数的参数

其中函数的参数分为：位置参数、默认参数、可变参数、关键字参数。详细信息请参考[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000)。

提示:
* 如果对某个函数的参数不清楚，可用内置函数`help()`显示其帮助文档。
    >若非交互式环境，还需调用`print()`函数。

## 成员访问
我们可用用`.`运算符访问对象的属性以及方法。

例如以下代码：
```python
text = "Beautiful is better than ugly."
print(text.count('t'))

# Result
# 4
```
这个例子就是访问并使用了`str`对象中的`count`方法。

# 安装和使用第三方库(pip,conda)

## 安装第三方库
* 若安装的为Anaconda的Python发行版，则其自带了许多常用的库，可以在cmd(或PowerShell)中键入`pip list`查看。
* 如果想要安装更多有趣的库，在cmd(或PowerShell)中输入`pip install libname`即可,libname为你所想安装库的名称。
* cmd的打开方式：`win+R`,然后在弹出的窗口中输入`cmd`即可

# 编码与解码
有关字符串编码的资料可以参考[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)。

## encode(编码)
我们可以对一个`str`对象，使用encode方法编码。

编码后得到的为一个`bytes`对象。

Example:
``` Python
text = '这里是中文'
# 注意在没有特殊业务需求时，强烈建议只使用UTF-8编码
# 使用UTF-8编码
print(text.encode('utf-8'))
# 使用GBK编码
print(text.encode('gbk'))

# Result
# b'\xe8\xbf\x99\xe9\x87\x8c\xe6\x98\xaf\xe4\xb8\xad\xe6\x96\x87'
# b'\xd5\xe2\xc0\xef\xca\xc7\xd6\xd0\xce\xc4'
```
## decode(解码)
与`encode`相对，我们可以对`bytes`对象进行解码。

**注意**：使用错误的解码格式进行解码，会导致程序抛出异常。

Example:
``` Python
btext = b'\xe8\xbf\x99\xe9\x87\x8c\xe6\x98\xaf\xe4\xb8\xad\xe6\x96\x87'
# 使用UTF-8正确的解码
print(btext.decode('utf-8')) # '这里是中文'
# 使用gbk错误的解码，会抛出UnicodeDecodeError
# btext.decode('gbk')
```