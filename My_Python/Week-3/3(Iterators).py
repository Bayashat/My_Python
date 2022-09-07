#   Technically, in Python, an iterator is an object which implements the iterator protocol,
# 迭代器
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

# 迭代器有两个基本的方法：iter() 和 next()
# which consist of the methods __iter__() and __next__().

                                    ###   <1> Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:

## 1)Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
it = iter(mytuple)

print(next(it))   # apple
print(next(it))   # banana
print(next(it))   # cherry

# 2
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 1  输出迭代器的下一个元素
print (next(it))   # 2



## 3)Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))   # b
print(next(myit))   # a
print(next(myit))   # n
print(next(myit))   # a
print(next(myit))   # n
print(next(myit))   # a
---------------------------------------------------------------------------------------------------
                        ###   <2> Looping Through an Iterator

## 1)Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

## 2)Iterate the characters of a string:
mystr = "banana"

for x in mystr:
  print(x)

The for loop actually creates an iterator object and executes the next() method for each loop.
------------------------------------------------------------------------------------------------------------------
                      ###   <3> Create an Iterator

To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
 __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法会返回下一个迭代器对象。

The __iter__() method acts similar with __init__ , you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.

# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter)) # 1
print(next(myiter)) # 2
print(next(myiter)) # 3
print(next(myiter)) # 4
print(next(myiter)) # 5
-----------------------------------------------------------------------------------
                                ###   <4> StopIteration
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
#  To prevent the iteration to go on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

# Stop after 20 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
--------------------------------------------------------------------------------------------------