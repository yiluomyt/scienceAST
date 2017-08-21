---
title: 静态页面爬虫
codes: {"Spider Code":"/tutorial/demo3.py", "Result":"/tutorial/demo3.txt"}
author: yiluomyt
---
# 静态页面爬虫
## Python 实践

首先我们来看下抓取网页的python代码
``` Python
# 导入第三方库requests
import requests

# 抓取github首页
# 使用requests库中提供的get方法
# HTTP请求为GET / HTTP/1.1
# host 为www.github.com
response = requests.get("http://www.github.com")

print('判断是否获取成功')
# 若输出True，则获取数据成功
print(response.ok)
```
至此，我们已经成功获取了github首页的数据信息。

下一步，我们该如何将这些数据输出呢？
``` Python
print('输出HTTP Status Code')
print(response.status_code)

print('输出网页的编码格式')
print(response.encoding)

print('输出Request的Headers')
print(response.request.headers)

print('输出Response的Headsers(由服务器返回)')
print(response.headers)

print('输出网页的内容')
print(response.content)

print('输出网页的HTML代码')
print(response.text)
```
以上最常用的就是response.text，我们之后对网页信息的提取也是基于HTML代码的。

### Question

1. 再抓取其他网站试试，看看是否也能成功获取到网页数据？

## 编码与解码

在对github进行抓取的时候，大家可能都是一帆风顺，但在抓取别的网站的时候，大家可能会碰到各种各样的_诡异的事情_。其中最多的，我相信应该是网页乱码，特别是对于中文网页而言。

在这里，就牵扯到一个编码问题。(编码是一种用二进制数据表示抽象字符的方式，utf8是一种编码方式。具体请看[百科](http://baike.baidu.com/link?url=sIzYsTLf7dLu1sOX4KhMYtxQOiOoiqXaATDqLv_1aJk0Flmj2Z3l8jbDqRUfnwGwpCwTv2cVp_n805zpe-Q77VsmPuzkKlH7WwUxTlzCTrW))

简单说，现在对于中文有两种常见的编码：
1. GBK
1. utf-8

使用错误的方式去解码就会产生乱码
>上一节中response.text是基于response.encoding对response.content解码产生的。
>即`response.text`等同于`response.content.decode(response.encoding)`
>
>若出现response.text乱码,可以尝试手动对response.content解码。

### 解决方案
该函数引用自[jieba分词](https://github.com/fxsjy/jieba)的源代码，经过小幅修改。
``` Python
def strdecode(sentence):
    # 判断所传入的sentence是否需要解码
    # 在Python 3中，str保存的即为unicode，所以不需要解码
    if not isinstance(sentence, str):
        try:
            # 尝试使用UTF-8解码
            sentence = sentence.decode('utf-8')
        except UnicodeDecodeError:
            # 使用GBK解码并忽略产生的错误
            sentence = sentence.decode('gbk', 'ignore')
    return sentence
```
>若想使用该函数自动判断解码方式的话，需要传入的对象为`response.content`。