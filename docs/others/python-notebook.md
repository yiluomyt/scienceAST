---
title: Python学习笔记
description: 隔壁老王|1303024845@qq.com
---

<<<<<<< HEAD
<<<<<<< HEAD
# dict和set
## dict
1. 使用key读取dict中的元素
    ``` Python
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  
    d['Michael']

    # Result
    # 95
    ```

1. 修改dict中的元素

    ``` Python
    d['Adam'] = 67  
    d['Adam']

    # Result
    # 67
    ```
    
1. dict中一个key只能对应一个value

1. 用in判断key是否存在

    例如：

    ``` Python
    'Thomas' in d

    # Result
    # False
    ```
1. 要删除一个key，用pop(key)方法，对应的value也会从dict中删除(是删除key,不是删除value)

    例如：`d.pop('Bob')`

1. 从dict中可以用get函数(get是成员函数)
=======
本文整理自[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
# dict和set
## dict
1. 使用key读取dict中的元素

    ``` Python
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  
    d['Michael']

    # Result
    # 95
    ```

1. 修改dict中的元素

    ``` Python
    d['Adam'] = 67  
    d['Adam']

    # Result
    # 67
    ```
1. dict中一个key只能对应一个value

1. 用in判断key是否存在

    例如：

    ``` Python
    'Thomas' in d

    # Result
    # False
    ```

1. 要删除一个key，用pop(key)方法，对应的value也会从dict中删除(是删除key,不是删除value)

    例如：`d.pop('Bob')`

1. 从dict中可以用get函数(get是成员函数)

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    例如：

=======
本文整理自[廖雪峰博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
# dict和set
## dict
1. 使用key读取dict中的元素

    ``` Python
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  
    d['Michael']

    # Result
    # 95
    ```

1. 修改dict中的元素

    ``` Python
    d['Adam'] = 67  
    d['Adam']

    # Result
    # 67
    ```
1. dict中一个key只能对应一个value

1. 用in判断key是否存在

    例如：

    ``` Python
    'Thomas' in d

    # Result
    # False
    ```

1. 要删除一个key，用pop(key)方法，对应的value也会从dict中删除(是删除key,不是删除value)

    例如：`d.pop('Bob')`

1. 从dict中可以用get函数(get是成员函数)

    例如：

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python
    d = {'a':2}  
    d.get('b')  
    d.get('a')

    # Result
    # None  1
    ```
<<<<<<< HEAD
<<<<<<< HEAD

## set
1. set和dict类似，也是一组key的集合，但不存储value。在set中没有重复的key(key不重复)

1. 要创建一个set，需要提供一个list作为输入集合
    例如：
    ``` Python
    s = set([1,2,3])
    print(s)

    # Result
    # {1,2,3}
    ```
1. 重复元素在set中自动被过滤

1. add(key)方法可以添加元素到set中(添加重复的没有效果)

    例如：
=======

=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
## set
1. set和dict类似，也是一组key的集合，但不存储value。在set中没有重复的key(key不重复)

1. 要创建一个set，需要提供一个list作为输入集合

    例如：

    ``` Python
    s = set([1,2,3])
    print(s)

    # Result
    # {1,2,3}
    ```

1. 重复元素在set中自动被过滤

1. add(key)方法可以添加元素到set中(添加重复的没有效果)

    例如：

<<<<<<< HEAD
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python 
    s = set([1,2,3])  
    s.add(4)   
    print(s)   
    
    # Result
    # {1,2,3,4}
    ```
<<<<<<< HEAD
<<<<<<< HEAD

1. remove(key)用于删除元素，用法与get一样

1. 两个set可做数学意义上的交集，并集等操作
    
    例如：

    ``` Pyhton  
    s1 = set([1,2,3])
    s2 = set([2,3,4]) 
    # 交集操作
    print(s1 & s2)
    # 并集操作
    print(s1 | s2)

    # Result
    # {2,3}  
    # {1,2,3,4}
    ```

## 可变和不可变对象
1. list可变，对list进行改变list变化，而对不可变对象例如str进行替换原str不变

# 函数
## 调用函数
1. 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

    例如：

    ``` Python
    a = abs
    print(a(-1))

    # Result
    # 1
    ```

2. 数据类型转换

    ``` Python
    int('123')
    # 123

    int(12.34)
    # 12

    float('12.34')
    # 12.34

    str(1.23)
    # '1.23'

    str(100)
    # '100'

    bool(1)
    # True

    bool('')
    # False
    ```

## 递归函数
在一个函数内部调用自身，这个函数就是递归函数。

例如：计算阶乘

``` Python
def fact(n):  
    if n == 1:  
        return 1  
    return n * fact(n-1) 
``` 

可能栈溢出，进行尾递归优化
``` Python 
def fact(n):  
    return fact_iter(n, 1)

def fact_iter(num, product)  
　　if num == 1:  
    　　　return product  
　　return fact_iter(num - 1, num * product)
```

# 高级特性
## 切片
1. 切片是**左闭右开**的

    切片格式：`L[start: stop: step]`

    ``` Python
    L = list(range(100))
    print(L)
    # 取前10个数
    print(L[:10])
    # 取后10个数
    print(L[-10:])
    # 取前11-20个数
    print(L[10:20])
    # 取指定步长的数
    print(L[:10:2])
    # 取所有数
    print(L[:])
    ```

2. 字符串进行切片

    例如：

    ``` Python  
    print('ABCDEFG'[:3])
    # 'ABC'

    print('ABCDEFG'[::2])
    # 'ACEG'
    ```

## 迭代
1. 定义：给定一个list或tuple，通过for循环来遍历这个list或tuple，这种遍历成为迭代。在Python中，迭代通过for......in来实现。只要是可迭代对象均可进行迭代，并非一定是list或tuple。

注意：
=======

1. remove(key)用于删除元素，用法与get一样

1. 两个set可做数学意义上的交集，并集等操作
    
    例如：

    ``` Pyhton  
    s1 = set([1,2,3])
    s2 = set([2,3,4]) 
    # 交集操作
    print(s1 & s2)
    # 并集操作
    print(s1 | s2)

    # Result
    # {2,3}  
    # {1,2,3,4}
    ```

## 可变和不可变对象

`list`可变，对`list`进行改变`list`变化，而对不可变对象,例如`str`进行替换原`str`不变

# 函数
## 调用函数

1. 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

    例如：
    
    ``` Python
    a = abs
    print(a(-1))

    # Result
    # 1
    ```

2. 数据类型转换

    ``` Python
    int('123')
    # 123

    int(12.34)
    # 12

    float('12.34')
    # 12.34

    str(1.23)
    # '1.23'

    str(100)
    # '100'

    bool(1)
    # True

    bool('')
    # False
    ```

## 递归函数
在一个函数内部调用自身，这个函数就是递归函数。

例如：计算阶乘

``` Python
def fact(n):  
    if n == 1:  
        return 1  
    return n * fact(n-1) 
``` 

可能栈溢出，进行尾递归优化

``` Python 
def fact(n):  
    return fact_iter(n, 1)

def fact_iter(num, product)  
　　if num == 1:  
    　　　return product  
　　return fact_iter(num - 1, num * product)
```

# 高级特性
## 切片

1. 切片是**左闭右开**的

    切片格式：`L[start: stop: step]`

    ``` Python
    L = list(range(100))
    print(L)
    # 取前10个数
    print(L[:10])
    # 取后10个数
    print(L[-10:])
    # 取前11-20个数
    print(L[10:20])
    # 取指定步长的数
    print(L[:10:2])
    # 取所有数
    print(L[:])
    ```

2. 字符串进行切片

    例如：

    ``` Python  
    print('ABCDEFG'[:3])
    # 'ABC'

    print('ABCDEFG'[::2])
    # 'ACEG'
    ```

## 迭代
1. 定义：给定一个`list`或`tuple`，通过`for`循环来遍历这个`list`或`tuple`，这种遍历成为迭代。在Python中，迭代通过`for...in`来实现。只要是可迭代对象均可进行迭代，并非一定是`list`或`tuple`。

注意：

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
* dict也可迭代

    ``` Python
    d = {'a': 1, 'b': 2, 'c': 3}
        for key in d:
            print(key)

    # a   b   c
    ```

<<<<<<< HEAD
    >默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
=======
    >默认情况下，`dict`迭代的是`key`。如果要迭代`value`，可以用`for value in d.values()`，如果要同时迭代`key`和`value`，可以用`for k, v in d.items()`
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

* 字符串可迭代

    ``` Python
    for ch in 'ABC':  
        print(ch)   
<<<<<<< HEAD

    # A   B   C
    ```

* 在for循环里，可以引用两个变量，这在Python里十分常见，例如：
``` Python
for x, y in [(1, 1), (2, 4), (3, 9)]:  
    print(x, y)

# 1 1
# 2 4
# 3 9
```

## 列表生成式
1. 用于创建list的生成式

    * 要生成list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`可以用`list(range(1, 11))`

    ``` Python
    list(range(1, 11))

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```

    * 用循环生成`[1x1, 2x2, 3x3, ..., 10x10]`

=======

    # A   B   C
    ```

* 在for循环里，可以引用两个变量，这在Python里十分常见
    >本质上是一个对于`tuple`进行装包和拆包的过程。

    例如：

    ``` Python
    for x, y in [(1, 1), (2, 4), (3, 9)]:  
        print(x, y)

    # 1 1
    # 2 4
    # 3 9
    ```

## 列表生成式
1. 用于创建list的生成式

    * 要生成list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`可以用`list(range(1, 11))`

    ``` Python
    list(range(1, 11))

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```

    * 用循环生成`[1x1, 2x2, 3x3, ..., 10x10]`
    
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python  
    l = []
    for x in range(1, 11):
        l.append(x * x)
    print(l)

    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

    * 用列表生成式生成②的结果

    ``` Python
    [x*x for x in range(1, 11)]

    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

<<<<<<< HEAD
    * 在列表生成式中使用if
=======
    * 在列表生成式中使用`if`
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    ``` Python
    [x * x for x in range(1, 11) if x % 2 == 0]

    # [4, 16, 36, 64, 100]
    ```

    * 利用两层循环生成全排列

    ``` Python
    [m + n for m in 'ABC' for n in 'XYZ']

    # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    ```

1. 列表生成式也可以使用两个变量来生成list

    ```Python  
    d = {'x': 'A', 'y': 'B', 'z': 'C' }
    print([k + '=' + v for k, v in d.items()])

    # Result
    # ['y=B', 'x=A', 'z=C']
    ```

1. 把一个list中所有的字符串变成小写

    ``` Python
    L = ['Hello', 'World', 'IBM', 'Apple']
    print([s.lower() for s in L])

=======

1. remove(key)用于删除元素，用法与get一样

1. 两个set可做数学意义上的交集，并集等操作
    
    例如：

    ``` Pyhton  
    s1 = set([1,2,3])
    s2 = set([2,3,4]) 
    # 交集操作
    print(s1 & s2)
    # 并集操作
    print(s1 | s2)

    # Result
    # {2,3}  
    # {1,2,3,4}
    ```

## 可变和不可变对象

`list`可变，对`list`进行改变`list`变化，而对不可变对象,例如`str`进行替换原`str`不变

# 函数
## 调用函数

1. 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

    例如：
    
    ``` Python
    a = abs
    print(a(-1))

    # Result
    # 1
    ```

2. 数据类型转换

    ``` Python
    int('123')
    # 123

    int(12.34)
    # 12

    float('12.34')
    # 12.34

    str(1.23)
    # '1.23'

    str(100)
    # '100'

    bool(1)
    # True

    bool('')
    # False
    ```

## 递归函数
在一个函数内部调用自身，这个函数就是递归函数。

例如：计算阶乘

``` Python
def fact(n):  
    if n == 1:  
        return 1  
    return n * fact(n-1) 
``` 

可能栈溢出，进行尾递归优化

``` Python 
def fact(n):  
    return fact_iter(n, 1)

def fact_iter(num, product)  
　　if num == 1:  
    　　　return product  
　　return fact_iter(num - 1, num * product)
```

# 高级特性
## 切片

1. 切片是**左闭右开**的

    切片格式：`L[start: stop: step]`

    ``` Python
    L = list(range(100))
    print(L)
    # 取前10个数
    print(L[:10])
    # 取后10个数
    print(L[-10:])
    # 取前11-20个数
    print(L[10:20])
    # 取指定步长的数
    print(L[:10:2])
    # 取所有数
    print(L[:])
    ```

2. 字符串进行切片

    例如：

    ``` Python  
    print('ABCDEFG'[:3])
    # 'ABC'

    print('ABCDEFG'[::2])
    # 'ACEG'
    ```

## 迭代
1. 定义：给定一个`list`或`tuple`，通过`for`循环来遍历这个`list`或`tuple`，这种遍历成为迭代。在Python中，迭代通过`for...in`来实现。只要是可迭代对象均可进行迭代，并非一定是`list`或`tuple`。

注意：

* dict也可迭代

    ``` Python
    d = {'a': 1, 'b': 2, 'c': 3}
        for key in d:
            print(key)

    # a   b   c
    ```

    >默认情况下，`dict`迭代的是`key`。如果要迭代`value`，可以用`for value in d.values()`，如果要同时迭代`key`和`value`，可以用`for k, v in d.items()`

* 字符串可迭代

    ``` Python
    for ch in 'ABC':  
        print(ch)   

    # A   B   C
    ```

* 在for循环里，可以引用两个变量，这在Python里十分常见
    >本质上是一个对于`tuple`进行装包和拆包的过程。

    例如：

    ``` Python
    for x, y in [(1, 1), (2, 4), (3, 9)]:  
        print(x, y)

    # 1 1
    # 2 4
    # 3 9
    ```

## 列表生成式
1. 用于创建list的生成式

    * 要生成list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`可以用`list(range(1, 11))`

    ``` Python
    list(range(1, 11))

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```

    * 用循环生成`[1x1, 2x2, 3x3, ..., 10x10]`
    
    ``` Python  
    l = []
    for x in range(1, 11):
        l.append(x * x)
    print(l)

    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

    * 用列表生成式生成②的结果

    ``` Python
    [x*x for x in range(1, 11)]

    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

    * 在列表生成式中使用`if`

    ``` Python
    [x * x for x in range(1, 11) if x % 2 == 0]

    # [4, 16, 36, 64, 100]
    ```

    * 利用两层循环生成全排列

    ``` Python
    [m + n for m in 'ABC' for n in 'XYZ']

    # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    ```

1. 列表生成式也可以使用两个变量来生成list

    ```Python  
    d = {'x': 'A', 'y': 'B', 'z': 'C' }
    print([k + '=' + v for k, v in d.items()])

    # Result
    # ['y=B', 'x=A', 'z=C']
    ```

1. 把一个list中所有的字符串变成小写

    ``` Python
    L = ['Hello', 'World', 'IBM', 'Apple']
    print([s.lower() for s in L])

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result
    # ['hello', 'world', 'ibm', 'apple']
    ```

### 生成器
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
1. 生成器：generator是一种一边循环一边生成的机制，不必创建完整的list，从而节省大量的空间

    创建一个generator可以将一个列表生成式的[]改为(),例如：

    ``` Python
    g = (x * x for x in range(10))
    print(g)
<<<<<<< HEAD

    #Result
    # <generator object <genexpr> at 0x1022ef630>
    ```

=======

    #Result
    # <generator object <genexpr> at 0x1022ef630>
    ```

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    可以利用next()函数打印generator中的每一个元素
    
    例如：

    ``` Python
    next(g)  
    # 0  
    next(g)  
    # 1
    ```

    但使用next函数过于麻烦，因此可以用for循环来解决问题。

    ``` Python
    g = (x * x for x in range(10))  
    for n in g:  
        print(n)
    
    # Result   
    # 0  
    # 1  
    # 4  
    # 9  
    # 16  
    # 25  
    # 36  
    # 49  
    # 64  
    # 81 
    ```

1. 用函数打印斐波那契数列

    ``` Python
    def fib(max):  
   　　　　　n, a, b = 0, 0, 1  
   　　　　　while n < max:  
   　　　　　　　print(b)  
   　　　　　　　a, b = b, a + b  
   　　　　　　　n = n + 1  
   　　　　　return 'done'
    ````

<<<<<<< HEAD
<<<<<<< HEAD
    将该函数变为generator，只需将print(b)改为yield(b),如下：
=======
    将该函数变为generator，只需将`print(b)`改为`yield b`
    
    例如：
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
    将该函数变为generator，只需将`print(b)`改为`yield b`
    
    例如：
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    ``` Python  
    def fib(max):  
    n, a, b = 0, 0, 1  
    while n < max:  
        yield b  
        a, b = b, a + b  
        n = n + 1  
    return 'done'
    ```

    这是**定义generator的另一种方法**，如果一个函数定义中包含yield关键字，那么这就不再是一个普通函数而是一个generator

<<<<<<< HEAD
<<<<<<< HEAD
1. 函数和generator的区别。函数是顺序执行，遇到return语句或者最后一行函数就返回。而变为generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

## 迭代器

1. list、tuple、dict、set、str这类集合数据类型和generator包括生成器和带yield的generator function均可以直接作用于for循环。这些可以直接作用于for循环的**对象**称为可迭代对象：Iterable
=======
1. 函数和generator的区别。函数是顺序执行，遇到return语句或者最后一行函数就返回。

    而变为generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

## 迭代器

1. list、tuple、dict、set、str这类集合数据类型和generator包括生成器和带yield的generator function均可以直接作用于for循环。
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    这些可以直接作用于for循环的**对象**称为可迭代对象：Iterable
    >可以使用`isinstance()`来判断一个对象是否为`Iterable`

    例如:

=======
1. 函数和generator的区别。函数是顺序执行，遇到return语句或者最后一行函数就返回。

    而变为generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

## 迭代器

1. list、tuple、dict、set、str这类集合数据类型和generator包括生成器和带yield的generator function均可以直接作用于for循环。

    这些可以直接作用于for循环的**对象**称为可迭代对象：Iterable
    >可以使用`isinstance()`来判断一个对象是否为`Iterable`

    例如:

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python
    from collections import Iterable
    isinstance([], Iterable)  
    # True  
    isinstance({}, Iterable)  
    # True  
    isinstance('abc', Iterable)  
    # True  
    isinstance((x for x in range(10)), Iterable)  
    # True  
    isinstance(100, Iterable)  
    # False  
    ```

1. 可以被next()函数调用并不断返回下一个值的**对象**称为迭代器：Iterator
<<<<<<< HEAD
    
    可以使用isinstance()判断一个对象是否是Iterator对象,
    
=======
    
    可以使用isinstance()判断一个对象是否是Iterator对象,
    
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    for example:

    ``` Python
    from collections import Iterator  
    isinstance((x for x in range(10)), Iterator)  
    # True  
    isinstance([], Iterator)  
    # False  
    isinstance({}, Iterator)  
    # False  
    isinstance('abc', Iterator)  
    # False
    ```
    
    >生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
    >
    >为什么list、dict、str等数据类型不是Iterator？
    >
    >因为Python的Iterator对象表示的是一个数据流,Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    >
    >Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 函数式编程
<<<<<<< HEAD
<<<<<<< HEAD
## 高阶函数(Higher-order function)
1. **变量可以指向函数**  
=======
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
## 高阶函数

1. **变量可以指向函数**

<<<<<<< HEAD
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    例如:

    ``` Python
    x = abs(-10)  
    print(x)
    # Result 
    # 10
    ```
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python
    f = abs
    print(f(-10))
    # Result
    # 10
    ```

1. **函数名也是变量**  
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    例如：

    ``` Python  
    abs = 10  
    abs(-10)  
    output:  
    Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
    TypeError: 'int' object is not callable
    ```
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    因为abs这个变量已经不指向求绝对值函数而是指向一个整数10

1. **传入函数**  
<<<<<<< HEAD
=======

    因为abs这个变量已经不指向求绝对值函数而是指向一个整数10

1. **传入函数**  

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数，例如:  

    ``` Python
    def add(x, y, f):  
    　　return f(x)+f(y)
    ```
<<<<<<< HEAD
<<<<<<< HEAD
## map/reduce
1. [Google](http://research.google.com/archive/mapreduce.html)
如果感兴趣可以通过Google的这篇论文来大概明白map和reduce的概念

1. map(func, *iterables),map后有两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回,例如:
=======

## map/reduce

1. MapReduce最早是由Google公司研究提出的一种面向大规模数据处理的并行计算模型和方法。灵感来自于函数式编程语言。

1. `map(func, *iterables)`

    map后有两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

    例如:
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

## map/reduce

1. MapReduce最早是由Google公司研究提出的一种面向大规模数据处理的并行计算模型和方法。灵感来自于函数式编程语言。

1. `map(func, *iterables)`

    map后有两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

    例如:
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    ``` Python
    def f(x):  
    　　　return x * x  
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  
    print(list(r))
    # Result  
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

<<<<<<< HEAD
<<<<<<< HEAD
    * map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x^2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串，例如： 
=======
    * map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的`f(x)=x^2`，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串，例如： 
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
    * map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的`f(x)=x^2`，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串，例如： 
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    ``` Python
    list(map(str,[1,2,3,4,5,6,7,8,9]))  
    # Result
    # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    ```

<<<<<<< HEAD
<<<<<<< HEAD
1.  reduce(function, sequence[, initial]),reduced的参数需要一个**具有两个参数的函数**和一个序列。  
reduce把结果继续和序列的下一个元素做累积计算，其效果就是:

    `reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`  
    (使用reduce时要导入：from functools import reduce)
=======
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
1.  `reduce(function, sequence[, initial])`

    reduced的参数需要一个**具有两个参数的函数**和一个序列。 

    reduce把结果继续和序列的下一个元素做累积计算，其效果就是:

    `reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`
    >使用reduce时要导入：`from functools import reduce`
<<<<<<< HEAD
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    reduce应用举例:

    * 将序列[1, 2, 3, 4, 5]变为整数12345   

    ``` Python   
    def fn(x, y):  
    　　return x*10+y  

<<<<<<< HEAD
<<<<<<< HEAD
    reduce(fn, [1, 2, 3, 4, 5])  
=======
    reduce(fn, [1, 2, 3, 4, 5])

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
    reduce(fn, [1, 2, 3, 4, 5])

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result  
    # 12345
    ```

    * 考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数: 

    ``` Python 
    from functools import reduce

    def str2int(s):  
    　　def fn(x, y):  
    　　　　return x * 10 + y  
    　　def char2num(s):  
    　　　　return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]  
    　　return reduce(fn, map(char2num, s))
    ```

    * 以上代码可用lambdah函数进行简化： 

    ``` Python 
    from functools import reduce

    def char2num(s):  
    　　return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]  

    def str2int(s):  
    　　return reduce(lambda x, y: x * 10 + y, map(char2num, s))  
    ```

    以上代码和int等效 

## filter
<<<<<<< HEAD
<<<<<<< HEAD
1.  filter()函数用于过滤序列，和map()类似，filter()也接收**一个函数和一个序列**。和map()不同的是，filter()把传入的函数依次作用于**每个元素**，然后根据返回值是True还是False决定保留还是丢弃该元素。
=======
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

1.  filter()函数用于过滤序列，和map()类似，filter()也接收**一个函数和一个序列**。
    
    和map()不同的是，filter()把传入的函数依次作用于**每个元素**，然后根据返回值是True还是False决定保留还是丢弃该元素。
<<<<<<< HEAD
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

1. 在一个list中删除偶数只保留奇数，实现方法如下:  

    ``` Python  
    def is_odd(n):  
    　　return n % 2 == 1

    list(filter(is_odd, [1, 5, 9, 6, 3, 7 , 8, 14]))  
    # Result  
    #[1, 5, 9, 3, 7]
    ```

1. 用filter求素数，实现代码如下:

* 用于生成一个无限的奇数列

    ``` Python 
    def odd_iter():  
    　　n = 1  
    　　while True:  
    　　　　n = n + 2  
    　　　　yield n
    ```

* 一个用于过滤不被之前奇数整除的新奇数
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python  
    def not_divisible(n):  
        return lambda x: x % n > 0 
    ```

* 查找素数函数 

    ``` Python 
    def primes():  
    　　yield 2  
    　　it = _odd_iter()  
    　　while True:  
    　　　　n = next(it)  
    　　　　yield n  
    　　　　it = filter(_not_divisible(n), it)  
    ```

* 设定限制  

<<<<<<< HEAD
<<<<<<< HEAD
``` Python
for n in primes():  
　　if n < 1000:  
　　　　print(n)  
　　else:  
　　　　break
```

## sorted
=======
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python
    for n in primes():  
    　　if n < 1000:  
    　　　　print(n)  
    　　else:  
    　　　　break
    ```

## sorted

<<<<<<< HEAD
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
1. Python内置的sorted()函数就可以对list进行排序：

    ``` Python
    sorted([36, 5, -12, 9, -21])
    output:
    [-21, -12, 5, 9, 36]
    ```

1. sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按**绝对值**大小排序：

    ``` Python
    sorted([36, 5, -12, 9, -21], key=abs)
    # Result
    # [5, 9, -12, -21, 36]
    ```

    其中key指定的函数作用于每一个元素上，再将返回值进行比较

1. 一个字符串排序：

    ``` Python
    sorted(['bob', 'about', 'Zoo', 'Credit'])
    # Result
    #['Credit', 'Zoo', 'about', 'bob']
    ```

    * 如果要使该排序忽略大小写只需将key后的映射修改一下：

    ``` Python
    sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)
    output:
    ['about', 'bob', 'Credit', 'Zoo']
    ```

1.  要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True:

    ``` Python
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
    # Result
    #['Zoo', 'Credit', 'bob', 'about']
    ```

## 返回函数
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
1. 将函数作为返回值：

    ``` Python
    def lazy_sum(*args):
        def sum():
            ax = 0
            for n in args:
                ax = ax + n
            return ax
        return sum
    ```

    * 通过这样的方法，调用lazy_sum时返回的不是结果而是函数:

    ``` Python
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)
    print(f())
<<<<<<< HEAD
<<<<<<< HEAD
=======
    
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
    
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result
    #<function lazy_sum.<locals>.sum at 0x101c6ed90>
    # Result
    # 25
    ```

1. >这种在一个函数中又定义了另一个函数内，内层函数可以引用外部函数的参数和局部变量，返回时相关变量和参数都保存在返回函数中的结构成为“闭包”。

    即使传入相同的参数，f1，f2结果互不影响：

    ``` Python
    1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
<<<<<<< HEAD
<<<<<<< HEAD
    f1==f2
=======
    f1 == f2

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
    f1 == f2

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result
    # False
    ```

1. 闭包
一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。下面是一个例子：

    ``` Python
    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i*i
            fs.append(f)
        return fs

    f1, f2, f3 = count()

    print(f1())
    print(f2())
    print(f3())
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result
    # 9
    # 9
    # 9
    ```

    >全部都是9。原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
<<<<<<< HEAD
<<<<<<< HEAD

    >返回闭包时牢记的一点就是：返回函数**不要引用任何循环变量**，或者后续会发生变化的变量。

    >如果一定要引用循环变量就再创建一个函数，用该函数的参数绑定循环变量当前的值。

## 匿名函数
1. 

``` Python
    list(map(lambda x : x * x , [1,5,6,8,9,7]))`
    # Result
    # [1, 25, 36, 64, 81, 49]
```

    用lambda表示匿名函数，冒号前的x表示函数参数，匿名函数**只能有一个表达式**，不用写return，返回值就是该表达式的结果。
    可以看出，lambda x : x * x 就是：

``` Python
    def f(x):
        return x * x
```

    也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

``` Python
    f = lambda x: x * x
    print(f(5))
    # Result
    # 25
```

## 偏函数
=======
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    >
    >返回闭包时牢记的一点就是：返回函数**不要引用任何循环变量**，或者后续会发生变化的变量。
    >
    >如果一定要引用循环变量就再创建一个函数，用该函数的参数绑定循环变量当前的值。

## 匿名函数

用lambda表示匿名函数，冒号前的x表示函数参数，匿名函数**只能有一个表达式**，不用写return，返回值就是该表达式的结果。

``` Python
list(map(lambda x : x * x , [1,5,6,8,9,7]))

# Result
# [1, 25, 36, 64, 81, 49]
```

可以看出，lambda x : x * x 就是：

``` Python
def f(x):
    return x * x
```

也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
<<<<<<< HEAD

``` Python
f = lambda x: x * x
print(f(5))

# Result
# 25
```

## 偏函数

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

``` Python
f = lambda x: x * x
print(f(5))

# Result
# 25
```

## 偏函数

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
1. 利用偏函数可以固定函数的参数
int()函数原本默认将字符串转换成10进制，我们可以通过修改其参数的形式将字符串转换为其他进制:

    ``` Python
    ptint(int('12345', base=8))
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result
    # 5349
    ```

1. 我们也可以通过定义一个新函数来解决这个问题：

    ``` Python
    def int2(x, base = 2):
        return int(x, base)

    print(int2('101101001'))
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result
    # 361
    ```

3. 可以通过functools.partial来创建一个偏函数，不需要我们自己定义int2():

    ``` Python
    import funtools
    int2 = functools.partial(int, base = 2)
    print(int2('10111110'))
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    # Result
    # 190
    ```

4. 创建偏函数时，可以接受*args ,**kw 这三个参数。上面的base = 2实际上将 **kw固定了，而下面的例子是将 *args中的一部分固定了：
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======

>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    ``` Python
    import functools
    max10 = functools.partial(max, 10)
    max10(2,6,8)
<<<<<<< HEAD
<<<<<<< HEAD
    # Result
    # 10
    ```
=======
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95

    # Result
    # 10
    ```

<<<<<<< HEAD
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
    当传入：
    `max10 = functools.partial(max, 10)`
    实际上会把10作为*args的一部分自动加到左边，相当于`args = (10, 2, 6, 8)
    max(*args)`

<<<<<<< HEAD
<<<<<<< HEAD
    这样可以使函数调用更加简单

# 模块
## 使用模块
1. >在Python中，一个.py文件就称为一个模块。使用模块大大提高了程序的可维护性，可以避免函数名与变量名的冲突。

2. !()[https://www.liaoxuefeng.com/files/attachments/001388366035986b515b38d149b4efaaac3f2c721813d2c000/0]
    >如图所示，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如图目录存放。

1. >引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz

4. >每一个包目录下都必须有一个__init__.py文件，如果没有这个文件python就会将其当作普通目录而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany

5. >类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：
https://www.liaoxuefeng.com/files/attachments/00138836605526535c9bebcbf414c3dae2430c50bbeef29000/0

6. >自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

# 面向对象编程
    >面向对象编程是一种程序设计思想，面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
    假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

``` Python
    std1 = { 'name': 'Michael', 'score': 98 }
    std2 = { 'name': 'Bob', 'score': 81 }
```

而处理学生成绩可以通过函数实现，比如打印学生的成绩：

``` Python
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
```

>如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
``` Python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print(bart.print_score())
print(lisa.print_score())
# Result
# Bart Simpson: 59
# Lisa Simpson: 87
```

## 类和实例
1. 定义类
    >面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
    >在Python中，定义类是通过class关键字。class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

1. 创建实例
    >定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过**类名+()**实现的：

    ``` Pyhton
    class Student(object):
        pass

    bart = Student()
    print(bart)
    output:
    <__main__.Student at 0x139aa74f048>
    ```

    可以看到，变量bart指向的就是一个Student的实例，后面的0x139aa74f048是内存地址，每个object的地址都不一样，而Student本身则是一个类。

1. 绑定实例的属性

    ``` Python
    bart.name = 'Bart Simpson'
    print(bart.name)
    # Result
    # 'Bart Simpson'
    ```

    >由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

    ``` Python
    class Student(object):

        def __init__(self, name, score):
            self.name = name
            self.score = score
    ```
    (注意：特殊方法"init"前后有**两个**下划线)

    注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

    有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去。

1. 和普通函数区别
    >和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

5. 数据封装

    我们可以通过外部函数来访问name和score这些数据：

    ``` Python
    def print_score(std):
        print('%s: %s' % (std.name, std.score))
    ```

    >但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：

    ``` Python
    class Student(object):

        def __init__(self, name, score):
            self.name = name
            self.score = score

        def print_score(self):
            print('%s: %s' % (self.name, self.score))
    ```

    >我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

    * 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

    ``` Python
    class Student(object):
        def get_grade(self):
            if self.score >= 90:
                return 'A'
            elif self.score >=60:
                return 'B'
            else:
                return 'C'
    print(bart.get_grade())
    # Result
    # 'C'
    ```
=======
    这样可以使函数调用更加简单
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
=======
    这样可以使函数调用更加简单
>>>>>>> 193f12d44d26eb6cd2dd3ecbb4ddcdf3fd970e95
