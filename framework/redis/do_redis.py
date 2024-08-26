# python实现对redis的连接
import redis

# 方式1: 创建一个Redis实例
# r  = redis.Redis(host="127.0.0.1", port="6379")
# r.set("name", "zhouyi")
# print(r.get("name"))

# 方式2: 连接池（一般这么用）
pool = redis.ConnectionPool(host="127.0.0.1", port="6379") # 创建连接池
r  = redis.Redis(connection_pool=pool) # 使用连接池

# 清除所有键
r.flushall()

# 字符串操作（字符串，hash，列表等，指的都是key-value中value的类型）
# 1. 增
r.set("name", "zy")
r.set("foo", "Bar")
r.set("age", 23)
r.set("need_to_delete", "ok")
res = r.setnx("foo", "XXX") # 不能重复赋值（分布式锁），返回Fasle
r.setex("temp", 10, "10") # 设置键的有效期
# 2. 删
r.delete("need_to_delete") # 和value的类型无关
# 3. 改
r.incrby("age", 10) # 自增 r.incr(age, 2)
r.decrby("age", 5) # 自减
r.append("foo", "001")
r.expire("name", 10)
# r.rename("name", "new_name")
# 4. 查
r.strlen("name")
print(r.keys())
print(r.get("foo"))
print(r.exists("name")) # 1 or 0
# 如何将字节字符串转换成unicode？需要解码，一般是utf-8编码的
print(str(r.type("name"), 'utf-8')) # b'string' （字节字符串: bytes string）



# hash操作
# 1. 增
r.hset("info", mapping={"name": "zhouyi", "age": 23, "need_to_delete": "ok", "do_not_delete": "ok"}) # 位置参数，可以按关键字参数来传递
# r.hmset("info", {"name": "zhouyi", "age": 23}) # 这个已经被弃用了
# 2. 删
r.hdel("info", "need_to_delete") # 删除hash中的某个键
# r.delete("info") # 删除key
# 3. 改
r.hset("info", "age", 25) # 
r.hincrby("info", "age", 5)
# 4. 查
print(r.hget("info", "name"))
print(r.hmget("info", "name", "age"))
print(r.hgetall("info"))

print(r.hkeys("info"))
print(r.hvals("info"))

print(r.hexists("info", "name"))



# list操作
# 1. 增
r.rpush("name_list", "zy", "zsy", "need_pop", "zkm")
r.lpush("name_list", "first")
r.linsert("name_list", "AFTER", "zy", "zy2")
# 2. 删
# r.lpop("name_list") # 删除第一个值
# r.rpop("name_list") # 删除最后一个值
r.lrem("name_list", 0, "need_pop")
# 3. 改
r.lset("name_list", 2, "wife")
# 4. 查
print(r.lrange("name_list", 0, -1))
print(r.lindex("name_list", 1))
print(r.llen("name_list"))



# set操作
# 1. 增
r.sadd("name_set", "zy", "zsy", "zkm", "need_to_delete")
# 2. 删
r.srem("name_set", "need_to_delete")
# r.spop("name_set") # 随机删除一个键
# 3. 改(集合改个P)
# 4. 查
print(r.smembers("name_set"))
print(r.srandmember("name_set", 2)) # 随机获取2个member
print(r.scard("name_set"))


# zset操作
# 1. 增
r.zadd("score_zset", {"zy": 90, "zsy": 100, "zy2": "80", "need_to_delete": 5})
# 2. 删
r.zrem("score_zset", "need_to_delete")
# r.zpopmin("score_zset")
# r.zpopmax("score_zset")
# 3. 改
r.zincrby("score_zset", 5, "zy2")
# 4. 查
r.zcard("score_zset")

print(r.zscore("score_zset", "zy2"))
print(r.zrange("score_zset", 0, -1, desc=reversed))
print(r.zrange("score_zset", 0, -1, withscores=True))
print(r.zrangebyscore("score_zset", 90, 100, withscores=True))
print(r.zcount("score_zset", 90, 100))







