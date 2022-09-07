'''    面向对象-继承
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Python面向对象的继承指的是多个类之间的所属关系，即⼦子类默认继承父类的所有属性和⽅法
'''
                                ### 1. Inheritance 继承
# 父类A
class A(object):
    def __init__(self):
        self.num = 1
    def info_print(self):
        print(self.num)
# 子类B
class B(A):
    pass

result = B()
result.info_print() # 1
# 在Python中，所有类默认继承object类，object类是顶级类或基类；其他⼦类叫做派生类

------------------------------------------------------------------------------------------------------------------------
                                ### 2.Single Inheritance 单继承
# 故事主线:一个煎饼果子老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎饼果⼦的技术。师⽗要把这套技术传授给他的唯一的最得意的徒弟。

# 1. 师父类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果⼦配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2. 徒弟类
class Prentice(Master):
    pass

# 3. 创建对象daqiu
daqiu = Prentice()

# 4. 对象访问实例属性
print(daqiu.kongfu)     # [古法煎饼果⼦配方]

# 5. 对象调用实例方法
daqiu.make_cake()       # 运用[古法煎饼果⼦配方]制作煎饼果子

------------------------------------------------------------------------------------------------------------------------
                                ### 3.Multiple Inheritance 多继承
# 故事推进：daqiu是个爱学习的好孩子，想学习更多的煎饼果⼦技术，于是，在百度搜索到黑⻢程序员，报班学习煎饼果⼦技术。

# 所谓多继承意思就是⼀个类同时继承了多个父类。
# 如果一个类继承多个父类,优先继承第一个父类的同名属性和方法

# 创建师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[⿊马煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果⼦')

# 定义徒弟类,继承 师傅类 和 学校类
class Prentice(School, Master):
    pass

# 用徒弟类创建对象,调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)     # [⿊马煎饼果子配方]
daqiu.make_cake()       # 运用[⿊马煎饼果子配方]制作煎饼果⼦

# 子类继承后,调用的时候调用的是自己的属性和方法

------------------------------------------------------------------------------------------------------------------------
                                ### 4. __mro__ 顺序
'''
会给出当前class所继承的父类都有哪些,以及这些父类的层级关系.'''

print(Prentice.__mro__)   # (<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)


