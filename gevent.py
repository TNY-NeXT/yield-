import gevent
import time


def foo():
    print('Running in foo', time.ctime())
    gevent.sleep(1)  # 这个gevent的sleep方法，是模拟IO阻塞任务，但是 time.sleep()是计算密集型任务
    print('Expilicit context switch to foo again', time.ctime())


def bar():
    print('Expilicit context to bar', time.ctime())
    gevent.sleep(2)
    print('Implicit context switch back to bar', time.ctime())


gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])
