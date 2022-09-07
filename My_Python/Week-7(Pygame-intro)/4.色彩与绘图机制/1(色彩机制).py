##################   1.色彩机制

                # 色彩表达:
                Pygame.Color
'''
Color 类用于表达色彩,使用RGB或RGBA色彩模式,A可选.
Color 类可以用色彩名字,RGBA值,HTML 色彩格式等方式定义pygame.examples.mask.main()

Color(name)         例如: Color("grey")

Color(r,g,b,a)      例如: Color(190,190,190,255)

Color(rgbvalue)     例如: Color("#BEBEBEFF")    16-进制格式
'''
                RGB
'''
RGB: 红绿蓝三个通道颜色组合,取值范围 0-255, 整数, 覆盖视力所能感知的所有颜色. 三个组合起来一共形成1600多万个颜色pygame.examples.mask.main()

white : (255,255,255)           白色
black : (0,0,0)                 黑色
grey  : (190,190,190)           灰色
darkgreen : (0,100,0)           深绿色
gold  : (255,215,0)             金色
voilet: (238,130,238)           紫罗兰
purple: (160,32,240)            紫色
'''
                RGBA
'''
是 RGB 的一种扩展, 增加了 Alpha 通道. 
Alpha 通道表示不透明度, 取值 0-255. 默认255
Alpha 通道越大,不透明度越高,255表示不透明.
'''
                pygame.Color 类:
pygame.Color.r      # 获得 Color 类的红色值 r
pygame.Color.g      # 获得 Color 类的绿色值 g
pygame.Color.b      # 获得 Color 类的蓝色值 b
pygame.Color.a      # 获得 Color 类的alpha值 a
pygame.Color.cmy    # 获取或设置 Color 对象表示的 CMY 值
pygame.Color.hsva   # 获取或设置 Color 对象表示的 HSVA 值
pygame.Color.hsla   # 获取或设置 Color 对象表示的 HSLA 值
pygame.Color.i1i2i3 # 获取或设置 Color 对象表示的 I1I2I3 值  
pygame.Color.correct_gamma()  # 应用一定的伽马值调整 Color 对象
pygame.Color.set_length()    #  设置 Color 对象的长度（成员数量）
pygame.Color.normalize  # 返回 Color 对象的标准化 RGBA 值.  将 RGBA 各通道值归一到0-1之间