# -*- coding: utf-8 -*-
# @Time :2021/8/11 20:23
# @Author : liufei
# @File :demo.PY

import queue

# 先入先出队列，先往队列中put的消息，在get时先取出。
q1 = queue.Queue(maxsize=3)  # maxsize指定队列中最大添加消息数

# 往队列中添加数据
q1.put(1, timeout=10)  # 默认添加数据等待，无时间限制
q1.put(2, block=False)  # 添加数据不等待，直接添加。若队列中无位置，添加失败报错
q1.put_nowait(3)  # 添加数据不等待，等同于put方法参数block=False

# 从队列中取数据
q1.get(timeout=3)  # 1。默认取数据等待，无时间限制
q1.get(block=False)  # 2。取数据不等待
q1.get_nowait()  # 3。取数据不等待，等同于get方法参数block=False

# 返回队列中消息的数量
q1.qsize()

# 判断队列是否为空，空-True
q1.empty()

# 判断队列是否以满，满-True
q1.full()

# task_done()，当队列中的每一个消息执行完毕取出后，都需要使用此方法给队列发一个信号，表示消息执行完毕。
# 然后join()方法才能判断队列中所有消息是否执行完毕，是否需要等待。
q1.task_done()
q1.task_done()
q1.task_done()

# join()，判断队列中所有消息是否已经执行完毕，完毕了代码继续向下执行。否则一直等待。
q1.join()

print("*********")

# 后入先出队列，最后往队列中put的消息，在get时先取出。
q2 = queue.LifoQueue()

# 优先级队列，根据优先级值取出，put的消息优先级数值越小，在get时先取出。
q3 = queue.PriorityQueue()

# 往优先级队列中添加数据时，需要以元组格式传入（优先级值，消息）
q3.put_nowait((2, 11))
q3.put((55, 7))
q3.put((1, 88))
print(q3.get())  # (1,88)
