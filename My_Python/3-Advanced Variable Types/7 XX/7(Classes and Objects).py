                                ### Class and object 类和对象
''' 面向对象和面向过程,是2种编程思想.编程思想是指对待同一个问题，解决问题的套路方式.
1.面向过程 : 注重的过程,实现的细节.亲历亲为

2.面向对象 : 关注的是结果,偷懒.
    * 3大特征:封装，继承，多态
'''
# 类是对一系列具有相同特征和⾏为的事物的统称，是⼀个抽象的概念
# 类和对象的关系: 用类去创建⼀个对象

'''
类(Class)由3个部分构成:
  * 类的名称 : 类名 
  * 类的属性 : 是它的特征，它有什么. or 一组数据
  * 类的方法 : 它的行为，它能做什么. 允许进行操作的方法(行为) / 在类中定义的函数
比如: 狗类的设计:
    类名 : Dog
    属性 : 品种，毛色，性别，名字，腿儿的数量
    方法(行为/功能) : 叫，跑，咬人，吃，摇尾巴
    
'''


                                ##   1.Create a Class
'''
class 类名():
  .....
  .....
  注意：类名要满足标识符命名规则，同时遵循⼤驼峰命名习惯。
'''

class Dogs():
  #  在类中定义的函数，称为方法.函数的所有特点，都可以在这儿使用.
  def play(self):
    print("Playinggggg")

# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5
--------------------------------------------------------------------------------------
                                ##   2.Create Object
# Now we can use the class named MyClass to create objects:
# Create an object named p1, and print the value of x:
'''
对象名  = 类名()
'''
dog1 = Dogs()
dog1.play()  # 用创建的对象调用方法: Playinggg

p1 = MyClass()
print(p1.x) # 5
----------------------------------------------------------------------------------------------------------------
                                ##   3. 添加和获取对象属性
                                ##   3.1 类外面添加对象属性
#  对象名.属性名 = 值

dog1.name = "Jack"
dog1.age = 2

                                ##  3.2 类外面获取对象属性
#  对象名.属性名
print(dog1.name)
print(dog1.age)

                                ##  3.3 类外面修改属性值 和添加一样: 存在加上修改，不存在加上添加
dog1.age = 3

                                ##  3.3 类里面获取对象属性
# self 作为类中方法的第一个形参，在通过对象调用函数时，不需要手动传递实参，是Python解释器自动将调用该方法的对象传递给self，所有self代表的是对象.

#   self.属性名
# 定义类
class Dogs():
  def play(self):
    print(f'{self.name} is playingg')
# 创建对象
dog1 = Dogs()
# 添加实例例属性
dog1.name = 'Jack'
dog1.age = 3

dog1.play()     # Jack is paying

----------------------------------------------------------------------------------------
                                  ## 4.在Python中， __xx__() 的函数叫做魔法方法，指的是具有特殊功能的函数。
                                  ## 4.1 The __init__() Function
## 作用 :
  # 1. 用来给对象添加属性,给对象属性一个初始值
  # 2. 代码的业务需求,每创建一个对象,都需要执行的代码可以写在__init__中
## 调用时机: 在创建对象之后,会立即调用.

class Dogs():
  def __init__(self):
    print('I am __init__')
    self.name = 'Kic'

dog1 = Dogs() # I am __init__   会在每创建对象时调用.
print(dog1.name)  # Kic
'''
注意：
__init__() ⽅法，在创建一个对象时默认被调⽤，不需要手动调用
__init__(self) 中的self参数，不需要开发者传递，python解释器器会自动把当前的对象引用传递过去。
'''

                      ## 4.1.2 带参数的__init__()
#思考：⼀个类可以创建多个对象，如何对不同的对象设置不同的初始化属性呢？
# 答：传参数。

class Dogs():
  def __init__(self,name,age):
    # 添加属性
    self.name = name
    self.age = age
# 创建对象
dog1 = Dogs("Jack",3)
dog2 = Dogs("Quen",2)

print(dog1.name, dog1.age)  # Jack 3
print(dog2.name, dog2.age)  # Quen 2

#  Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

-----------------------------------------------------------------------------------------------------------------------
                                    ### 4.2 __str__()
## 应用:
  # 1. 打印对象的时候,输出一些属性信息
  # 2. 需要将对象转换为字符串类型的时候

## 调用时机:
  # 1. 'print(对象)' 打印对象时,会自动调用,打印输出的结果是__str__方法的返回值
  # 2. 'str(对象) 类型转换,将自定义对象转换为字符串的时候,会自动调用.
## 注意点 : 方法必须返回一个字符串, 只有self一个参数

# 当使用print输出对象的时候，默认打印对象的内存地址。如果类定义了了__str__ ⽅方法，那么就会打印从在这个⽅法中 return 的数据

                            ##### 1) 定义 __str__ 前
class Dogs():
  def __init__(self,name,age):
    # 添加属性:
    self.name = name
    self.age = age

# 创建对象
dog1 = Dogs("Jack",3)
print(dog1)    # <__main__.Dogs object at 0x0000029365BB8FD0>  没有定义__str__方法, print(对象) 默认输出对象的引用地址

str_dog = str(dog1)
print(str_dog)  # <__main__.Dogs object at 0x0000029365BB8FD0>  没有定义__str__方法, 类型转换,赋值的也是引用地址.

                            #### 2） 定义 __str__ 后
class Dogs():
  def __init__(self,name,age):
    # 添加属性:
    self.name = name
    self.age = age

  def __str__(self):
    # 必须返回一个字符串
    return f"Dog's name is {self.name}, age is {self.age}"

# 创建对象
dog1 = Dogs("Jack",3)
print(dog1)   # Dog's name is Jack, age is 3

-----------------------------------------------------------------------------------------------------------------------
                                      ### 4.3 当删除对象时，python解释器器也会默认调用__del__() ⽅法。
# add : 引用计数 : 是 Python 内存管理的一种机制,是指一块内存有多少变量.
    # 1.当一个变量,引用一块内存时,引用计数+1
    # 2.当删除一个变量,或这个变量不在引用这块内存,引用计数+1
    # 3.当引用计数为0的时候,这块内存被删除,内存中的数据被销毁.
my_list = [1,2]  # 1
my_list1 = my_list # 2
del my_list    # 1
del my_list1   # 0
## 调用时机:
  # 对象在内存被销毁删除的时候会自动调用__del__方法
    # 1.程序代码运行结束(引用计数为0),在程序运行过程中,创建的所有对象和变量都会被删除销毁
    # 2.使用 ‘del 变量‘ 将这个对象的引用计数变为0. 会自动调用 __del__

## 应用场景:
  # 对象被删除销毁的时候,要书写的代码可以写在 __del__ 中
class Dogs():
  def __init__(self,name,age):
    # 添加属性:
    self.name = name
    self.age = age

  def __str__(self):
    # 必须返回一个字符串
    return f"Dog's name is {self.name}, age is {self.age}"

  def __del__(self):
    print("I am __del__")

# 创建对象
dog = Dogs("Jack",3)   # 程序结束调用: I am __del__

--------------------------------------------------------------------------------------------------------------------
                                  ###   5.Object Methods
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
----------------------------------------------------------------------------------------------------------------------------------------
#   5.Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
------------------------------------------------------------------------------------------------------------------------------------------
                                        ###   6.The self Parameter
# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
--------------------------------------------------------------------------------------------------------------------------------------------------
                                        ###   7.Modify Object Properties
# You can modify properties on objects like this:

p1.age = 40
---------------------------------------------------------------------------------------------------------------------------------------------
                                       ###   8.Delete Object Properties
Delete the age property from the p1 object:

del p1.age
---------------------------------------------------------------------------------------------------------------------------------------
#   9.Delete Objects
Delete the p1 object:

del p1
---------------------------------------------------------------------------------------------------------------------------------
#   10.The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass
------------------------------------------------------------------------------------------------------------------------------------------