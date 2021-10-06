import redis
from config import*

r = redis.Redis(host=my_host, port=my_port, 
                password=my_password)

# r.mset({'name':'sid','age':'17'})

r.psetex('name', 1000, "siddharth") # milisecond

# print(r.get('name'))
# print(r.get('age'))

if (r.exists('name')):
    print(r.get('name'))
else:
    "cannot find the key"
