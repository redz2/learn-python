# 人类使用文本，计算机使用字节序列


# str
# 从str中获取的字符是Unicode，python字符串默认就是Unicode码
# 文本 === 字节序列
# 编码
a = 'abcd'
b = a.encode('utf-8')
# 解码
b.decode('utf-8')

# bytes
# 从字符串创建二进制序列类型
cafe = bytes('cafe', encoding='utf-8')


# 如何找出字节序列的编码规则？
# 必须有人来告诉你