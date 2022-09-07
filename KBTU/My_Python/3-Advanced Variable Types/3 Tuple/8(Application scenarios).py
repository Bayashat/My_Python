"""
                < 8 > Application scenarios / 应用场景
    元组在开发时,更多的应用场景是:
* 作为函数的 "参数" 和 "返回值": 一个函数可以接受 "任意多个参数", 或者 一次返回 "多个数据"
* 格式字符串: 格式化字符串后面的 () 本质上就是 元组 : %(name, age)
* 让列表不可以修改, 以保护数据安全

"""
info_tuple = ("Bayashat", 19)
print("My name is %s, I'm %d years old" %info_tuple)    # My name is Bayashat, I'm 19 years old

