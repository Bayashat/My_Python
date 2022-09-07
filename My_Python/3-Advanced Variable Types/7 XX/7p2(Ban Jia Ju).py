##                                      Practice-2 : 搬家具
# 1 需求
    # 将小于房子剩余面积的家具摆放到房子中
# 2 步骤分析
    # 需求涉及两个事物：房⼦和家具，故被案例涉及两个类：房子类 和 家具类。

# 1.家具类
class Furniture():
    def __init__(self, name, area):
        # 家具名字:
        self.name = name
        # 家具占地面积:
        self.area = area
# 2.房子类:
class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余⾯积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房⼦坐落于{self.address}, 占地面积{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        # 如果 家具占地面具 <= 房子剩余面积: 可以搬入
        # 否则: 提示⽆法容纳
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            # 家具搬⼊后，房屋剩余⾯积 = 之前剩余面积 - 该家具面积
            self.free_area -= item.area
        else:
            print('家具太大，剩余⾯积不足，⽆法容纳')


bed = Furniture('双人床', 6)
jia1 = Home('北京', 1200)

print(jia1)                 # 房⼦坐落于北京, 占地面积1200, 剩余面积1200, 家具有[]

jia1.add_furniture(bed)
print(jia1)                 # 房⼦坐落于北京, 占地面积1200, 剩余面积1194, 家具有['双人床']

sofa = Furniture('沙发', 10)
jia1.add_furniture(sofa)
print(jia1)                 # 房⼦坐落于北京, 占地面积1200, 剩余面积1184, 家具有['双人床', '沙发']

ball = Furniture('篮球场', 1500)
jia1.add_furniture(ball)    # 家具太大，剩余⾯积不足，⽆法容纳
print(jia1)                 # 房⼦坐落于北京, 占地面积1200, 剩余面积1184, 家具有['双人床', '沙发']
