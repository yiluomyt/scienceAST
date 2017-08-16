---
title: XPath与CSS 选择器
qrcode: True
codes: {"Example":"/tutorial/demo4-2.py", "Result":"/tutorial/demo4-2.txt"}
author: yiluomyt
---

# XPath与CSS 选择器

与正则表达式不同，XPath和CSS 选择器不是用来处理通用文本的工具。而是针对网页HTML结构进行筛选的工具，两者用法相似但又有所区别。
* XPath 本身是用于处理XML结构文本的工具，因为HTML与XML结构类似，所以亦可处理HTML文本。
* CSS 选择器(CSS Selector) 本身是用于筛选CSS标记的工具，因为现在的网页大多都使用了CSS，所以在处理HTML文本时亦有不错的效果。

关于[XPath](http://www.w3school.com.cn/xpath/xpath_intro.asp)和[CSS 选择器](http://www.w3school.com.cn/cssref/css_selectors.asp)的语法网上已经有不少教程，所以在此就不再赘述。我们主要来看XPath和CSS 选择器在Python中的使用方法。

在本篇中，主要使用到两个第三方库`BeautifulSoup`和`lxml`，可以使用`pip`安装。

# XPath
我们可以通过`lxml`库来使用XPath语句

Example:
``` Python
# 导入lxml中的etree类
from lxml import etree
# html为包含网页html代码的str对象
# 由HTML创建文档树
selector = etree.HTML(html)
# 使用XPath语句
xpath_result = selector.xpath('//*[@class="content-list-item"]/div/div/a/text()')
# 打印XPath结果
print("Here is the result of xpath:")
for i, item in enumerate(xpath_result):
    print("%-2d: %s" % (i, item))
```

# CSS 选择器
我们可以通过`BeautifulSoup`来使用CSS 选择器

Example:
``` Python
# 由HTML创建soup对象,使用lxml解析器
soup = BeautifulSoup(html, 'lxml')
# 使用CSS 选择器
# select 所返回的为包含bs4.element.Tag的list
css_result = soup.select('.content-list-item > div > div > a')
# 提取Tag的text
css_result_text = [tag.text for tag in css_result]
# 打印CSS Selector结果
print("Here is the result of css selector:")
for i, item in enumerate(css_result_text):
    print("%-2d: %s" % (i, item))
```