## 访问限制
1. 如下是之前定义Student这个类的代码:

    ``` Python
    class Student(object):

        def __init__(self, name, score):
            self.name = name
            self.score = score

        def print_score(self):
            print('%s %s' % (self.name, self.score))

        def get_grade(self):
            if self.score >= 90:
                return 'A'
            elif self.score >= 60:
                return 'B'
            else:
                return 'C'

    Name = input()
    score = int(input())
    bart = Student(Name, score)
    print(bart.name)
    print(bart.score)
    print(bart.get_grade())
    ```

1. 如果要使内部属性不被外部访问，可以把属性的名称前加**两个**下划线，这样变量名就变成了私有变量(private)。现在我们来做一些修改:

    ``` Python
    class Student(object):

        def __init__(self, name, score):
            self.__name = name
            self.score = score

        def print_score(self):
            print('%s : %s' % (self.__name, self.__score))
    ```

    这时再输入`bart.__name`时,就会出现  
    `Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'Student' object has no attribute '__name'`  
    意思就是不能访问了。

1. 那么如果要访问name和score怎么办呢？我们可以在类中定义用于访问的函数:

    ``` Python
    class Student(object):
        ...
        def get_name(self):
            return self.__name

        def get_score(self):
            return self.__score
    ```

    这样输入`print(bart.get_name())`或`print(bart.get_score)`就可以访问name和score了

1. 特别注意，在Python中，例如__xxx__的变量名是**可以直接访问**的特殊变量，不是private变量

1. 一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，一个下划线的意义是不要随意访问。

1. 很污的比喻
    在一个实例里：  
    __girl表示“我是贞女，你不能上我”  
    _girl表示“你虽然可以上我，但你应该把我看做贞女”  
    girl表示“我是荡妇，谁都可以上我”  
    但是python仍然可以用_实例名__girl强上贞女

## 继承和多态
1. 我们先来定义一个类:

    ``` Python
    class Animal(object):

        def run(self):
            print('Animal is running...')
    ```

    这是一个叫作Amimal的类，其中有一个可以用于打印的run方法。

2. 现在我们来继承:

    ``` Pyhton
    class Dog(Animal):
        pass

    class Cat(Animal):
        pass
    ```

    现在完成了一个最简单的继承，我们可以通过如下方式打印出结果:

    ``` Python
    dog = Dog()
    print(dog.run())

    cat = Cat()
    print(cat.run())
    
    # Result
    # Animal is running...
    # Animal is running...
    ```

    可以发现Dog和Cat是Animal的子类，但它们在没有定义run方法的情况下自动拥有了run方法。这就是继承的一个好处:子类拥有父类的全部方法。

1. 可是子类如果和父类总是显示一样显然不符合逻辑，因此我们可以用到继承的第二个好处:当子类和父类存在一样的方法时，子类的会覆盖父类的。

    ``` Python
    class Dog(Animal):

        def run(self):
            print('Dog is running...')


    class Cat(Animal):
        def run(self):
            print('Cat is running...')
        
    dog = Dog()
    print(dog.run())

    cat = Cat()
    print(cat.run())

    # Result
    # Dog is running
    # Cat is running
    ```

    这个继承的好处就叫多态。

1. 对多态的解释  
    #isinstance()函数可以判断一个变量是否是某个类型

    ``` Python
    c = Dog()
    b = Animal()
    print(isinstance(c, Dog))
    print(isinstance(c, Animal))
    print(isinstance(b, Dog))

    # Result
    # True
    # True
    # False
    ```

    可以看出子类的数据类型是属于父类的，但反过来不行。

1. 理解多态的好处，我们再来定义一个接受Animal类型的函数run_twice()和一个Animal的子类Bird

    ``` Python
    class Animal(object):

        def run(self):
            print('Animal is running...')

        def run_twice(self):
            self.run()
            self.run()

    class Dog(Animal):
        def run(self):
            print('Dog is running...')

    class Bird(Animal):
        def run(self):
            print('Bird is flying...')

    dog = Dog()
    bird = Bird()
    print(dog.run_twice())
    print(run_twice(Bird()))

    # Result
    # Dog is running...
    # Dog is running...
    # Bird is flying...
    # Bird is flying...
    ```

    可以发现新增一个Animal的子类不必对run_twice()进行更改，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

    >多态的好处就是，当我们需要传入Dog、Cat、Bird时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Bird都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思.

## 获取对象信息
1. 可以用`type()`来判断对象类型

    ``` Python
    print(type(123))
    print(type('str'))
    print(type(abs))

    # Result
    # <class 'int'>
    # <class 'str'>
    # <class 'builtin_function_or_method'>
    ```

1. 对于class的继承关系来说,type就很不方便，这时就可以用isinstance()

    ``` Python
    class Animal(object):
        pass


    class Dog(Animal):
        pass


    class Husky(Dog):
        pass

    a = Animal()
    d = Dog()
    h = Husky()

    print(isinstance(a, Husky))
    print(isinstance(h, Animal))
    print(isinstance(a, object))

    # Result
    # False
    # True
    # True
    ```

1. 能用`type()`判断的基本类型也可以用`isinstance()`判断

1. 使用`dir()`可以获得一个对象所有属性和方法

    ``` Python
    print(dir('str'))

    # Result
    # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    ```

1. 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。  
    在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的:

    ``` Python
    print(len('ABC'))
    print('ABC'.__len__())

    # Result
    # 3
    # 3
    ```

    剩下的都是普通属性或方法，比如`lower()`返回小写的字符串:

    ``` Python
    print('ABC'.lower())

    # Result
    # 'abc'
    ```

1. 我们可以通过`getattr()`、`setattr()`和`hasattr`来直接操作一个对象的状态。先定义一个对象:

    ``` Python
    class MyObject(object):
        def __init__(self):
            self.x = 9
        
        def power(self):
            return self.x * self.x

    obj = MyObject()
    ```

    接着测试对象的属性:

    ``` Python
    print(hasattr(obj, 'x'))
    print(obj.x)
    print(hasattr(obj, 'y'))
    setattr(obj, 'y', 19)
    print(hasattr(obj, 'y'))
    print(getattr(obj, 'y'))

    # Result
    # True
    # 9
    # False
    # True
    # 19
    ```

    可以传入一个default参数，如果属性不存在就返回默认值:

    ``` Python
    print(getattr(obj, 'z', 404))

    # Result
    # 404
    ```

1. 用`hasattr()`和`getattr()`还可以获得对象的方法，代码和获取属性的只有单引号内部变成了方法名，其余都一样。获得的方法可以赋值:

    ``` Python 
    fn = getattr(obj, 'power')
    print(fn())

    # Result
    # 81
    ```

## 实例属性和类属性
1. 可以通过实例变量给实例绑定属性:

    ``` Python
    class Example(object):
        def __init__(self, name):
            self.name = name

    e = Example('Sam')
    e.score = 100
    ```

    如果Example类中要绑定一个属性可以这样操作:

    ``` Python
    class Example(object):
        name = 'Sam'    
        # 这样就绑定了类属性
    e = Example()

    print(e.name)
    print(Example.name)

    e.name = 'Bob'
    print(e.name)
    print(Example.name)

    del e.name
    print(e.name)

    # Result
    # Sam
    # Sam
    # Bob
    # Bob
    # Sam
    ```

    可以看出实例属性优先级比类属性优先级高，有实例属性的情况下类属性是被屏蔽的。但如果将实例属性删除类属性就显现出来了。
