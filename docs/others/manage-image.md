# 对图片简单的操作
1. 图片的打开与显示
    这是一种使用操作系统自带的图片浏览器来打开图片:

    ``` Python
    from PIL import Image
    img = Image.open('E:/图片/d05b32b9a75440b11e03e1e21e4b0482.jpg')
    img.show()

    # Result
    ```
    ![Jensen Ackles](http://pic.baike.soso.com/ugc/baikepic2/4486/20170824011024-718290859_jpg_500_691_30289.jpg/0)

    还可以用程序来绘制图片(这里使用一个matplotlib的库来绘制图片进行显示):

    ``` Python
    from PIL import Image
    import matplotlib.pyplot as plt
    img=Image.open('E:/图片/d05b32b9a75440b11e03e1e21e4b0482.jpg')
    plt.figure("Jensen Ackles")
    plt.imshow(img)
    plt.show()

    # Result
    # 用matplotlib打开的“丁丁”
    ```

1. figure默认是带axis的，如果没有需要，我们可以关掉:`plt.axis('off')`

1. 打开图片后，可以使用一些属性来查看图片信息:

    ``` Python
    print(img.size)
    print(img.mode)
    print(img.format)

    # Result
    # (500, 691)
    # RGB
    # JPEG
    ```

1. 保存图片  
    `img.save('d:/dd.jpg')`


