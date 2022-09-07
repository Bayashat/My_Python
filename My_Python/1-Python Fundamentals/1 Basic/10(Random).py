import random

x = random.randint(1,3) # 从 1-3 的区间产生随机数. Contains 3

                                 ## 1.Random functions:
#  1.choice(seq)	 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数

#  2.randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1

#  3.random()	          随机生成下一个实数，它在[0,1)范围内

#  4.seed([x])	          改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed

#  5.shuffle(lst)	      将序列的所有元素随机排序

#  6.uniform(x, y)	      随机生成下一个实数，它在[x,y]范围内
