# Python编程思想
1. 基本的程序设计模式(IPO)
* input -> process（模块化设计，拆分成更小的IPO）-> output
```
输入（自己主动去获取数据，提供API添加配置信息）
系统（处理逻辑）
输出（自己主动发送消息、邮件、日志，提供API返回数据）
```
2. 解决复杂问题的有效方法（自顶向下）
* 模块化设计
    * 抽象出关键的数据结构
        * 数据输入 -> 抽象基类
        * 逻辑处理 -> 中间过程数据抽象基类
            * 分层缺失: 各种功能写在一个类里
        * 数据输出 -> 抽象基类

# 编程思想
* 结构化
* 关注点分离
* 抽象
    * 优雅的编程始于抽象（无需关注实现细节，基于提供的抽象来构建应用）
    * 在合适的抽象上去思考问题（如果有人给你提供了抽象，你就得按照人家的规定来使用，不然就有点不识好歹了，除非你牛逼自己去实现）
* 封装
    * 封装是抽象的实现形式
    * 将功能封装成python的模块或golang的包（工具库 or 层次结构）
* 复用
    * 没有封装就没有复用
* 分治
    * 如果一个问题无法解决，尝试分解问题（如何解决一个问题？）
* 组合
    * 单一逻辑能够处理的问题有限，需要组合起来
* 缓存
* 解耦
    * 高内聚，低耦合

# FP vs OOP
* FP
    * 变量不可变 -> 无状态 -> 更适合执行并发操作
    * 少量的数据，大量的简短函数，很容易添加新的函数
    * 但是，如果要添加数据，就很费劲
* OOP
    * 数据和操作绑定
    * 有状态 -> 方法带来副作用 -> 更适合和实际生活中的场景联系起来 -> 容易看懂
    * 如果一个概念，必须包含多个接口才完整，没有理由分离成一个个函数
* 函数应不应该称为数据的一部分？
    * 如果函数和数据的关系紧密呢？
    * 如果函数是比较通用的呢？