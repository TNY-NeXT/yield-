import queue
import time

def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(2)


def producer():
    next(con)
    next(con2)
    n = 0
    while n < 5:
        n += 1
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
        con.send(n)
        con2.send(n)



if __name__ == '__main__':
    con = consumer('c1')
    con2 = consumer('c2')
    p = producer()

#协程应该是串行执行的，只不过因为它会记住上下文环境，所以提高了执行速度。
