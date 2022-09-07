#############   4.事件处理函数
'''
pygame 共提供了8个事件处理函数,分为3组
'''
# 1).处理事件:
pygame.event.get()
pygame.event.poll()
pygame.event.clear()

# 2).操作事件队列:
pygame.event.set_blocked()
pygame.event.get_blocked()
pygame.event.set_allowed()

# 3).生成事件:
pygame.event.post()
pygame.event.Event(type, dict)  


                            ################ 1).处理事件:
                    # 1.1
pygame.event.get()
'''
从事件队列中获得事件列表,即获得所有被队列的事件
'''
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
'''
增加参数,获得某类或某些类事件:  '''
pygame.event.get(type)
pygame.event.get(typelist)

                    # 1.2
pygame.event.poll()
'''
从事件队列中获得一个事件
'''
while True:
    event = pygame.event.poll()
'''
事件获取将从事件队列中删除
如果事件队列为空,则返回 event.NOEVENT   '''


                    # 1.3
pygame.event.clear()
'''
从事件队列中删除事件,默认删除所有事件.
该函数与 pygame.event.get() 类似,区别仅是不对事件进行处理.

可以增加参数,删除某类或某些类事件:              '''
pygame.event.clear(type)
pygame.event.clear(typelist)

'''
*********************************************************************************************************************************************
'''
                                #################  2.操作事件队列
''' 事件队列同时仅能存储128个事件.当队列满时,更多事件将被丢弃. 
    设置事件队列能够缓存事件的类型                          '''

                        
                            pygame.event.set_blocked(type or typelist)
'''
控制哪些类型事件不允许被保存到事件队列中
'''

                            pygame.event.set_allowed(type or typelist)
'''
控制哪些类型事件允许被保存到事件队列中
'''

                            pygame.event.get_blocked(type)
'''
测试某个事件类型是否被事件队列所禁止
如果事件类型被禁止,则返回 True, 否则返回 False
'''


'''
*********************************************************************************************************************************************
'''
                                ##############   3.生成事件:

                                pygame.event.post(Event)
'''
产生一个事件,并将其放入事件队列
一般用于放置用户自定义事件 (pygame.USEREVENT)
也可以用于放置用户自定义事件(如鼠标或键盘等), 给定参数.
'''

                                pygame.event.Event(type, dict)
'''
创建一个给定类型的事件
其中,事件的属性和值采用字典或类型复制,属性名采用字符串形式
如果创建已有事件,属性需要一致
'''