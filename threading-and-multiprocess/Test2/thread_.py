import threading
import time
from pie_test import*

start = time.perf_counter()


def cal():
    a = 1+5
    while True:
        a += a
        if a >= 100000000000000000000000000:
            break
    # print(a)


    b = 9
    while True:
        b += b
        if b >= 10000000000000000000000000000000:
            break
    c = b - a
    # print(c)
    d = c - 1000000000
    lst = []
    for _ in range(10000):
        d += d
        lst.append(d)

    time.sleep(0.1)
    r = lst[::-1]
    return r
   


threads = []

for _ in range(100):
    t = threading.Thread(target=cal)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()     

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")