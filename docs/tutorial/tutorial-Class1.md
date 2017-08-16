---
title: 准备工作
---

# 开发环境

所有Demo代码均在以下环境中正确运行
* Windows 10 家庭版 1703(Creator Update)
* Python 3.6.0(Anaconda3 4.3.1 64-bit)

# 所需工具

* [Anaconda3](https://www.continuum.io/downloads)
* [Anaconda3 国内镜像](https://mirrors.tuna.tsinghua.edu.cn/#)
* [Visual Studio Code](https://code.visualstudio.com/)
* [git(可选)](https://git-scm.com/downloads)
* [Chrome](http://www.google.cn/chrome/browser/desktop/)
* [Firefox](http://www.firefox.com.cn/)
    * [Firebug](https://addons.mozilla.org/zh-CN/firefox/addon/firebug/)
    * [FirePath](https://addons.mozilla.org/zh-CN/firefox/addon/firepath/)

# 安装配置环境

1. Anaconda3根据提示安装即可
1. VS Code 在安装结束后，需再安装Python插件(发布者@Don Jayamanne)
1. 更新Python第三方库`conda update --all`
    >官方服务器在海外速度可能较慢，可参考[本文](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)设置国内镜像。

---
Firebug和FirePath在安装完Firefox后，使用Firefox打开相应链接，即可安装。
>安装顺序为 Firefox -> Firebug -> FirePath

# 推荐软件

1. [Postman](https://www.getpostman.com/)
    >一款用于测试API的工具
1. [Jupyter Notebook](http://jupyter.org/)
    >一个非常强大的交互式执行环境，不单单可以交互式执行代码，还可以将过程保存下来，以多种形式进行分享。
    >
    >在Anaconda中自带该程序，可以在 [开始]菜单中直接运行。