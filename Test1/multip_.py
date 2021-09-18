import requests
import multiprocessing
import time
from pie_test import*


# api-endpoint
URL = "https://piencrypt.herokuapp.com/test/sid86"


start = time.perf_counter()
def req():
    # request to url
    r = requests.get(url = URL)
    data = r.json()
    secret_code = data['PiEncrypt']
    print(f"Secret = {secret_code}")


    
def cal():
    a = 1+5
    while True:
        a += a
        if a >= 100000000000000000000000000:
            break



    b = 9
    while True:
        b += b
        if b >= 10000000000000000000000000000000:
            break
    c = b - a

    d = c - 1000000000
    print(f"Return value = {d}")



p1 = multiprocessing.Process(target=cal)
p2 = multiprocessing.Process(target=unittest.main)
p3 = multiprocessing.Process(target=req)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()


finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")