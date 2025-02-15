# protobuf
* Protocol Buffer: 数据结构序列化和反序列化的框架（用于数据传输和存储）
    * 语言无关，平台无关
    * 更加轻量
* protobuf vs json vs pickle
    * 都是数据交换格式
    * protobuf使用二进制数据（有点类似pickle，但是没有语言的限制）
        1. 编写.proto文件
        2. 通过protoc编译器生成对应语言的代码
    * json使用文本格式（传输或存储一般还需使用utf-8编码成字节序列）
    * pickle序列化指的是将python对象转换成二进制字节流的过程（传输两端必须都是python，这个限制太大了）
* [python-betterproto](https://github.com/danielgtaylor/python-betterproto)
