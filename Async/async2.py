import asyncio
import time


import requests

start = time.perf_counter()

 # api-endpoint
URL = "https://piencrypt.herokuapp.com/test/sid86"

async def main():
    task = asyncio.create_task(cal())
    print("Process Starting")

    await asyncio.sleep(3)
    # request to url
    r = requests.get(url = URL)
    data = r.json()
    secret_code = data['PiEncrypt']
    print(f"Secret = {secret_code}")

    await asyncio.sleep(0.5)

    # return value of cal
    return_val = await task

    d = return_val - 1000000000
    print(f"Return value = {d}")



async def cal():
    a = 1+5
    while True:
        a += a
        if a >= 100000000000000000000000000:
            break
    # print(a)

    await asyncio.sleep(0.1)

    b = 9
    while True:
        b += b
        if b >= 10000000000000000000000000000000:
            break
    c = b - a
    # print(c)
    return c






async def request_url():
           # request to url
    
    await asyncio.sleep(1)

    r = requests.get(url = URL)
    data = r.json()
    secret_code = data['PiEncrypt']
    return secret_code



asyncio.run(main())

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")