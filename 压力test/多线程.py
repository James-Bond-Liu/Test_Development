class Demo():
    import threading
    a = 0
    def one(self):
        global a
        for i in range(100000000):
            a += 1

    def two(self):
        global a
        for j in range(100000000):
            a += 1

    t1 = threading.Thread(target=one)
    t2 = threading.Thread(target=two)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(a)

if __name__ == '__main__':
    for i in range(4):
        print(i)