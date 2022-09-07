###################   11.classmethod()
'''
Converts a method into a class method
'''

class Person:
  name = 'Person 1'
  age = 20

  @classmethod         # here you can put your values
  def sample(cls, gpa): # class method
    print(gpa)

  def get_age(self): # instance method
    return self.age

p = Person()

# you can call the class method in 2 ways: 

Person.sample(55)

'''
class A(object):
    bar = 1
    def func1(self):  
        print ('foo') 
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()   # 调用 foo 方法
 
#  A.func1() Error : because 需要实例化 need instance
A.func2()  # 不需要实例化
'''

