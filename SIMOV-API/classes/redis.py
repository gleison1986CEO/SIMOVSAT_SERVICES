
import redis

class redis_server():
    def URI():
       ## REDIS
       
       return redis.Redis(host='localhost', port=6379, db=0)