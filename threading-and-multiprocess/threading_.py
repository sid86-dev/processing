import threading
import time


start = time.perf_counter()

def cal_1():
    print("Starting task 1")
    num = 5
    while True:
        num += num
        if num >= 10000000000000000000000000000:
            break
    time.sleep(1)
    print(f'Done Process 1 at {num}')


def cal_2():
    print("Starting task 2")
    num = 5
    while True:
        num += num
        if num >= 1000000000000000000000:
            break
    time.sleep(1)
    print(f'Done Process 2 at {num}')

threads = []

t1 = threading.Thread(target=cal_1)
t2 = threading.Thread(target=cal_2)

t1.start()
t2.start()

t1.join()
t2.join()


finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")
