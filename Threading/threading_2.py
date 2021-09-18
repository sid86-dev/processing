import requests
import threading
import time


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
    # print(a)


    b = 9
    while True:
        b += b
        if b >= 10000000000000000000000000000000:
            break
    c = b - a
    # print(c)
    d = c - 1000000000
    print(f"Return value = {d}")


t1 = threading.Thread(target=cal)
t2 = threading.Thread(target=req)

t1.start()
t2.start()

t1.join()
t2.join()


finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")