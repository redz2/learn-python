## 关系型数据库和非关系型数据库
* RMDBS: 关系型数据库
* NoSQL: not only sql，泛指非关系型数据库
    * 只要不使用SQL语句进行数据库操作的，都是NoSQL

## Redis（Remote Dictionary Service，远程字典服务）
* Redis支持数据持久化（基于RDB和AOF），用来替代Memcache
* 数据类型
    1. string
    2. hash
    3. list
    4. set（无序，去重）
    5. zset（有序，去重）
    6. custom

```
redis = {
    "name": "zhouyi",
    "age": "23",
    "scor": [1,2,3],
    "info": {
        "hobby": "singh"
    },
    "s": {item1, item2},
    "zs": 
}
```
* 应用场景
    1. 缓存系统
    2. 计数器
    3. 消息队列
    4. 社交网络
    5. 排行榜
    6. 发布订阅

### key操作
keys *
keys *a*
exists age
type age
del name age
flushall # 清空所有键，慎用
ttl name # -1表示不会过期,-2表示没有该key
expire name 200
rename name myname

默认16个库，select 0


### 字符串
```
set name zhou
set age 23

# 不能重复赋值（分布式锁）
setnx name yi
del name

# 设置有效期（10s后过期，优惠券，验证码）
setex name 10 yi
set name yi
expire name 10

# 批量设置和批量查询
mset name zhou age 18
mget name age

# 追加内容
append name "yi"

# 数字字符串自增自减（必须是一个数字字符串）
set count 90
incr count 
decr count
incrby count 10
decrby count 10

# 计算字符串长度（如果是中文呢？）
strlen name

# 比特流操作
setbit mykey 7 1 -> 00000001
setbit mykey 6 1 -> 00000011
getbit mykey 7
countbit mykey start end # 统计有几位设置为1

# 和直接使用set修改的区别，体会一下
set name "a" # 01100001 -> 01100010
setbit name 6 1
setbit name 7 0
get name -> "b"

签到系统
```

### list（列表：成员必须是string）
1. 增
    * lpush names zhangsan # zhangsan -> ["zhangsan"]
    * rpush names lisi # ["zhangsan", "lisi"] <- lisi
    * linsert names after "zhangsan" "zhou" # 如果有多个张三，从左到右找到第一个张三，在后面添加一个zhou
2. 删
    * lpop names # 获取并删除第一个列表成员
    * rpop names # 获取并删除最后一个列表成员
    * lpop 和 rpush # 实现先入先出的队列
    * lrem names 3 zhouyi # 按照值来删除，从上往下数
    * lrem names -2 zhouyi # 按照值来删除，从下往上数
    * lrem names 0 zhouyi # 全删掉
3. 改
    * lset names 0 zsy # 按索引设置值
4. 查
    * lindex names 0
    * lrange names 0 -1 # 查看
    * lrange names -2 1
    * llen names

### hash（info是一个hash）
1. 增
    * hset info field value # 设置hash的键值对(按照键值键值的方式来呈现)
    * hset info age 13 hobby sing  class 4 # 同时设置多个键的值
2. 删
    * hdel info field # 删除hash中的某个键
3. 改
    * hincrby info field 10 # 怎么没有减的操作命令？
    * hset info field new_value # 重新设置新的value
4. 查
    * hget info field # 获取一个键的值
    * hmget info field1 field2 # 获取多个键的值
    * hgetall info # 获取所有键的值
    * hkeys info # 获取所有的键
    * hvals info # 获取所有的值
    * hexists info field # 判断hash中是否存在某个键

### set（无序集合：去重）
1. 增: sadd authors zsy zy xk
2. 删
    * srem authors xk
    * spop authors (随机取)
3. 改（集合中改个p）
4. 查: 
    * smembers authors
    * scard authors # 获取总个数

#### 集合之间的关系
* 交集 sinter
* 差集 sdiff
* 并集 sunion
* 补集 ？？？

### zset（有序集合）
1. 增
    * zadd key score1 value1 score2 value2 (排行榜)
2. 删
    * zrem key member1 member2
    * zpopmin key [count] # 删除指定数量的成员，从低的开始删
    * zpopmax key [count] # 删除指定数量的成员，从高的开始删
3. 改
    * zincrby key score member
4. 查
    * zcard key (获取zset长度)

    * zrangebycore key min max （权重区间）
    * zrevrangebycore key max min
    * zrange key start end
    * zrevrange key start end
        * zrange key 0 -1 (从低到高全部成员)

    * zscore key member (获取某一个成员的权重值)

    * zrank key member (获取正向排名)
    * zrevrank key member（获取反向排名）

    * zcount key min max (获取在指定score区间成员数)


