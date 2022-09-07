                                    pygame.time
# Pygame 中用于监控时间的模块。

                                    1).函数
pygame.time.get_ticks()     # 获取以毫秒为单位的时间
pygame.time.wait()          # 暂停程序一段时间
pygame.time.delay()         # 暂停程序一段时间
pygame.time.set_timer()     # 在事件队列上重复创建一个事件
pygame.time.Clock()         # 创建一个对象来帮助跟踪时间
'''
Pygame中的时间以毫秒（1/1000秒）表示。大多数平台的时间分辨率有限，大约为10毫秒。该分辨率（以毫秒为单位) 以常量 TIMER_RESLUTION 给出。
'''

                                    2).函数详解
                                pygame.time.get_ticks()
'''
获取以毫秒为单位的时间

get_ticks() -> milliseconds

返回自 pygame_init() 调用以来的毫秒数。在pygame初始化之前，这将始终为0。
'''
                                pygame.time.wait() 
'''
暂停程序一段时间

wait(milliseconds) -> time

将暂停一段给定的毫秒数。此函数会暂停进程以与其他程序共享处理器。等待几毫秒的程序将消耗非常少的处理器时间。它比pygame.time.delay() 函数稍微准确一些。

这将返回实际使用的毫秒数。
'''
                                pygame.time.delay() 
'''
暂停程序一段时间

delay(milliseconds) -> time

将暂停一段给定的毫秒数。此功能将使用处理器（而不是休眠），使用 pygame.time.wait() 以使延迟更准确。

这将返回实际使用的毫秒数。
'''
                                pygame.time.set_timer() 
'''
在事件队列上重复创建一个事件

set_timer(eventid, milliseconds) -> None

将事件类型设置为每隔给定的毫秒数显示在事件队列中。第一个事件将在经过一段时间后才会出现。

每种事件类型都可以附加一个单独的计时器。在 pygame.USEREVENT 和 pygame.NUMEVENTS 中使用该值更好。

要禁用事件的计时器，请将milliseconds参数设置为0。
'''
                                pygame.time.Clock()  
'''
创建一个对象来帮助跟踪时间

Clock() -> Clock
'''
pygame.time.Clock.tick()  ——  更新时钟
pygame.time.Clock.tick_busy_loop()  ——  更新时钟
pygame.time.Clock.get_time()  ——  在上一个tick中使用的时间
pygame.time.Clock.get_rawtime()  ——  在上一个tick中使用的实际时间
pygame.time.Clock.get_fps()  ——  计算时钟帧率

# 创建一个新的Clock对象，可用于跟踪一段时间。时钟还提供了几个功能来帮助控制游戏的帧速率。

                                tick() 
'''
更新时钟

tick(framerate=0) -> milliseconds

注：

应该每帧调用一次此方法。它将计算自上一次调用以来经过的毫秒数。

如果传递可选的帧率参数，该函数将延迟以使游戏运行速度低于每秒给定的滴答数。这可以用于帮助限制游戏的运行时速度。通过每帧调用 一次 Clock.tick(40)，程序将永远不会超过每秒40帧。

请注意，此函数使用SDL_Delay函数，该函数在每个平台上都不准确，但不会占用太多CPU。如果你想要一个准确的计时器，请使用tick_busy_loop，并且不介意咀嚼CPU。
'''
                                tick_busy_loop()
'''
更新时钟

tick_busy_loop(framerate=0) -> milliseconds

注：

应该每帧调用一次此方法。它将计算自上一次调用以来经过的毫秒数。

如果您传递可选的帧率参数，该函数将延迟以使游戏运行速度低于每秒给定的滴答数。这可以用于帮助限制游戏的运行时速度。通过每帧调用 一次 Clock.tick_busy_ioop(40)，程序将永远不会超过每秒40帧。

请注意，此函数使用 pygame.time.delay(，在繁忙的循环中使用大量CPU以确保时间更准确。

pygame 1.8.0中的新功能。
'''
                            get_time() 
'''
在上一个tick中使用的时间

get_time() -> milliseconds

前两次调用 Clock.tick() 之间传递的毫秒数。
'''
                            get_rawtime() 
'''
在上一个tick中使用的实际时间

get_rawtime() -> milliseconds

类似于 Clock.get_time()，但不包括  Clock.tick() 延迟限制帧速率时使用的任何时间。
'''
                            get_fps()  

计'''
算时钟帧率

get_fps() -> float

计算游戏的帧速率（以每秒帧数为单位）。它是通过平均最后十次调用来计算的  Clock.tick() 。
'''