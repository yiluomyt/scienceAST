---
title: 正则表达式
codes: {"re.match Example":"/tutorial/demo4-re-match.py"}
author: yiluomyt
---

# 网页信息提取

在一个网页中包含着很多信息，而我们所需要的往往只是其中的一部分，所以我们在网络上采集信息时，需要对信息进行清洗提取。

常用的方式主要有一下三种：
* 正则表达式
* XPath语句
* CSS选择器

# 正则表达式

>正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

以上介绍引自[百度百科](https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215?fr=aladdin#2)

可以看到，正则表达式就是一种对应规则的过滤。

关于[正则表达式的教程](http://www.runoob.com/regexp/regexp-tutorial.html)网上有许多，这里就不再赘述，我们着重来看正则表达式在Python中的用法。

## re

[re](https://docs.python.org/3/library/re.html)是Python标准库提供的，用于处理正则表达式的库。

### match

`re.match(pattern, string, flags=0)`

`match`函数会从`string`的第一个字符开始，匹配`pattern`所给出的规则：
* 若在匹配过程中，遇到一个不符合规则的字符，直接结束匹配，并返回`None`
* 若在匹配过程中，`string`长度小于`pattern`所要求长度，结束匹配过程，并返回`None`
* 若没有发生上述两种情况，成功匹配完的，则会返回一个包含匹配的字符串以及其在原字符串中的位置信息的对象，不再继续向后匹配。

如以下代码:

```Python
import re

# 匹配成功
match1 = re.match(r'hello', 'hello world!')
# 匹配失败
match2 = re.match(r'hello world', 'hello')
# 匹配失败
match3 = re.match(r'python', 'hello python')
# 命名分组，匹配成功
match4 = re.match(r'(?P<data>\d{4}-\d{1,2}-\d{1,2}) (\d{2}:\d{1,2}:\d{1,2})', '2017-07-20 11:22:33')

if match1:
    # 可以用成员函数group()来获取所匹配的字符串
    # match1.group()与下一行等价
    print(match1.group(0))
    # 可以用成员函数span()来获取所匹配字符串在原字符串中的起始位置与结束位置
    # match1.span()与下一行等价
    print(match1.span(0))
else:
    print('match1 fail!')

if match2:
    print(match2.group())
else:
    print('match2 fail!')

if match3:
    print(match3.group())
else:
    print('match3 fail!')

if match4:
    # 返回所有分组
    print(match4.groups())
    # 返回所有命名分组
    print(match4.groupdict())
else:
    print('match4 fail!')
```

运行结果:
```Python
hello
(0, 5)
match2 fail!
match3 fail!
('2017-07-20', '11:22:33')
{'data': '2017-07-20'}
```

### search

`re.search(pattern, string, flags=0)`

`search`函数的工作方式与`match`相似，区别是`search`不是从字符串的第一个字符开始匹配，而是搜索整个字符串，直到找到第一个满足`pattern`的字符开始匹配。

Example(来自[官方文档](https://docs.python.org/3/library/re.html#search-vs-match)):
```Python
re.match("c", "abcdef")    # No match
re.search("^c", "abcdef")  # No match
re.search("^a", "abcdef")  # Match
```


### split

`re.split(pattern, string, maxsplit=0, flags=0)`

`split`函数能以可匹配的子字符串作为分割界限，以`list`形式返回分割后在字符串。

参数`maxsplit`表示最大分割次数

Example:
```Python
re.split(r'-', '2017-07-21')

# Result
# ['2017', '07', '21']
```

### findall

`re.findall(pattern, string, flags=0)`

`findall`函数能搜索整个字符串，以`list`形式返回所有匹配的字符串。

Example:
```Python
re.findall(r'\d+', '2017-07-21')

# Result
# ['2017', '07', '21']
```

### finditer

`re.finditer(pattern, string, flags=0)`

`finditer`和`findall`作用相同，只不过是以迭代器形式返回结果。

### sub

`re.sub(pattern, repl, string, count=0, flags=0)`

`sub`函数可以将原字符串中所匹配的子字符串用新字符串替换。
* `pattern` 正则表达式
* `repl` 替换字符串
* `string` 原字符串
* `count` 替换次数，为0时全部替换

Example:
```Python
re.sub(r'world', 'python', 'hello world')

# Result
# 'hello python'
```

### flags

可以看到之前所以的函数中都有一个参数`flags`，它是用来配置正则表达式的匹配模式的。
>取值可以使用按位或运算符`|`表示同时生效，比如`re.I | re.M`。(来自[静觅](http://cuiqingcai.com/977.html))

 * `re.I`(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
 * `re.M`(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为
 * `re.S`(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
 * `re.L`(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
 * `re.U`(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
 * `re.X`(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。



 ## 思考

 1. `re`模块的使用方式有多种，请掌握至少一种使用方法
 1. 使用正则表达式提取[中关村新闻](http://news.zol.com.cn/)的新闻标题