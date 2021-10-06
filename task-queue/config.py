import redis

r = redis.Redis(host='redis-12393.c10.us-east-1-4.ec2.cloud.redislabs.com', port=12393, 
                password='J9BmwAzuZuFNHY6Xg6u2pXRci0dJRnkH')

# r.mset({'name':'sid','age':'17'})

r.psetex('name', 1000, "siddharth") # milisecond

# print(r.get('name'))
# print(r.get('age'))

if (r.exists('name')):
    print(r.get('name'))
else:
    "cannot find the key"