---
title: Python 进阶
author: yiluomyt
---

本篇部分代码参考自《Natural Language Processing with Python》

# 引用对象的赋值
请考虑下列代码运行结果
``` Python
empty = []
nested = [empty, empty, empty]
empty.append('1')
print(nested)
```
正常结果为：`[['1'], ['1'], ['1']]`

## 解释
可以使用内建的`id`函数来查看对象的标识符
``` Python
empty = []
nested = [empty, empty, empty]
print(id(empty))
print([id(item) for item in nested])
# 输出结果为
# 2442757933960
# [2442757933960, 2442757933960, 2442757933960]
```

可以看到`nested`中的三个元素均指向`empty`对象， 所以在对`empty`对象进行修改后，`nested`中元素的值也会相应的改变。

## 思考
以下三种操作有什么不同
``` Python
l = ['1', '2', '3']
# Operation 1
l1 = l
# Operation 2
l2 = l[:]
# Operation 3
import copy
l3 = copy.deepcopy(l)
```

# 判断相等
请分析以下代码中的三种判断区别
``` Python
list1 = ['1']
list2 = ['1']
# Operation 1
print(list1 == list2)
# Operation 2
print(list1 is list2)
# Operation 3
print(isinstance(list1, list))
```
正确输出结果为：
``` Python
True
False
True
```

## 解释
上述代码中的三种判断作用分别如下：
1. 判断`list1`和`list2`值是否相等
2. 判断`list1`与`list2`是否引用同一个对象
3. 判断`list1`是否为`list`类的一个实例

# 列表生成式与生成器表达式

## 区别
* 列表生成式返回的是所得结果的`list`
* 生成器表达式返回的是包含计算公式的`generator`

## 应用
请解决以下问题：
> 输出`list1`中最长的字符串
``` Python
list1 = ['Beautiful', 'is', 'better', 'than', 'ugly', '.', 'Explicit', 'is', 'better', 'than', 'implicit', '.', 'Simple', 'is', 'better', 'than', 'complex', '.']
```

实现一
``` Python
longest = ''
for item in list1:
    if len(item) > len(longest):
        longest = item

print(longest)
```

实现二
``` Python
# 生成器表达式作为函数参数时，可以省去()
maxlen = max(len(item) for item in list1)
print([item for item in list1 if len(item) == maxlen])
```

运行后可以发现， 这两种实现都可以达到任务要求，但显然后一种实现更贴近人的思维。

## 思考
请解决下列问题
> 1. 计算`list1`中的平均词长
> 1. 统计`list1`中各个字母出现的次数

# 生成器与高阶函数

## 函数形式的生成器
创建一个生成器的方法有多种，在不能用生成器表达式简单创建的时候，我们可以考虑使用函数的形式来创建生成器。
``` Python
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'End'

for number in fib(10):
    print(number)
```
我们可以看到一个函数形式定义的生成器与普通的函数的差别就是使用了`yield`语句。

该语句表示：
1. 返回`yield`后表达式的值
2. 在下一次调用`next()`时，从此继续运行(`for`循环即一个不断调用`next`的过程)

但是，我们会发现我们没有收到fib中`return 'End'`的值。实际上，在生成器结束生成时，会将返回值储存在`StopIteration`中抛出。

运行以下代码：
``` Python
try:
    f = fib(1)
    # 此处已经完成了所有生成
    next(f)
    # 再次调用将会抛出StopIteration
    next(f)
except StopIteration as e:
    print('The value in StopIteration is ', e.value)
```
我们得到结果：`The value in StopIteration is  End`

## 高阶函数
在Python中函数是第一类对象(First-Class Object)，即`function`可以和其他类型(如`int`, `str`, `list`等)一样在运算时创建、储存、销毁。

所以，简单说，接受一个函数作为参数的函数就是高阶函数。

请看以下代码：
``` Python
def myAdd(x, y, f):
    return f(x) + f(y)

print(myAdd(-1, 10, abs))
```

再看一个更为实际的应用：
> 实现对`list1`中的字符串按长度排序

``` Python
list1 = ['Beautiful', 'is', 'better', 'than', 'ugly', '.', 'Explicit', 'is', 'better', 'than', 'implicit', '.', 'Simple', 'is', 'better', 'than', 'complex', '.']

print(sorted(list1, key=lambda x:len(x)))
```

## 函数式编程&惰性计算
正如我们所知，在生成器中保存的仅仅是计算公式，仅当调用`next()`时才会计算下一个值。这就非常符合函数式编程中惰性计算的思维。

我们也可以更具这样特性来实现一些有趣的东西。

请实现下列要求：
> 1. 创建一个表示所有奇数的生成器
> 1. 创建一个表示所有质数的生成器

这里给出第一个要求的实现
``` Python
# 注意此处生成器是无限生成器
# 若将其直接用于循环时，需注意退出条件
import itertools

odds = filter(lambda x: x % 2 == 1, itertools.count(1))

for number in odds:
    if number > 100:
        break
    else:
        print(number)
```

# Zen of Python
当你在交互式环境中输入`import this`就会出现那段经典的Zen of Python

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 思考
`import this`只会在第一次时显示Zen of Python

但我们可以发现刚刚`import`的`this`对象有两个属性`this.s`和`this.d`，分别为一段加密的文本和一个用于解密的字典。

请解密并再体会这段文字