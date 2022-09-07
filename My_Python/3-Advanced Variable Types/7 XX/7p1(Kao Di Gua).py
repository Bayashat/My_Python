#                            Practice-1: 烤地⽠
# 需求主线：
# 1. 被烤的时间和对应的地⽠瓜状态：
    # 0-3分钟：⽣的
    # 3-5分钟：半⽣不熟
    # 5-8分钟：熟的
    # 超过8分钟：烤糊了
# 2. 添加的调料：
    # ⽤户可以按⾃己的意愿添加调料

class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜的⽅法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'

    def add_condiments(self, condiment):
        """添加调料料"""
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地⽠烤了{self.cook_time}分钟, 状态是{self.cook_static}, 添加的调料有{self.condiments}'


# 创建对象,并调用对应的示例方法
digua1 = SweetPotato()
print(digua1)   # 这个地瓜烤了0分钟, 状态是生的, 添加的调料料有[]

digua1.cook(2)
print(digua1)   # 这个地⽠烤了2分钟, 状态是生的, 添加的调料料有[]

digua1.cook(2)
digua1.add_condiments('辣椒面儿')
print(digua1)   这个地⽠烤了4分钟, 状态是半生不熟, 添加的调料有['辣椒面儿']