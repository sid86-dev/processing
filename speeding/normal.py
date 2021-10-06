import random
import math
import time

def cal_(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 2)
    return z

start = time.time()

cal_(10000000)

end = time.time()

print(f"finished in {end-start} seconds") # 5.5 sec