import redis


r = redis.StrictRedis(host='192.168.171.213', port=6379)
print(r.get('yoyo'))
