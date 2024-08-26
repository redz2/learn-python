import re
import reprlib

# 1. 可迭代对象
# iter(obj) -> 返回一个迭代器！！！
# 显式: 实现__iter__()，显式返回一个迭代器
# 隐式: 实现__getitem__()，调用iter()后，python创建一个迭代器，并且从0开始获取元素（序列为什么可以迭代的原因）

# 如何检查对象是否可迭代？
# 为什么iter()比较好？因为isinstance(x, abc.Iterable)没有考虑到__getitem__()方法

# 2. 迭代器
# __next__() 返回下一个可用的元素（必须要实现此方法）！！！
# __iter__() 返回self，比如在for循环中会隐式调用iter()，需要返回一个迭代器，所以迭代器也是可迭代的

# 什么时候停止迭代？如何处理异常？for和while处理异常的区别？
# 如果尝试失败，Python抛出异常，"Object is not iterable"

# 3. 生成器


RE_WORD = re.compile('\w+')

### Sentence第一版
class SentenceV1():
    
    """单词序列"""
    
    def  __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    # 如果实现了__getitem__()，iter()会返回迭代器
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        # repr生成大型数据的简略字符串表示形式
        return "Sentence(%s)" % reprlib.repr(self.text)
        






### Sentence第二版

class SentenceV2():
    
    """可迭代对象"""
    
    """
    为什么不在SentenceV2中实现__next__()方法呢?
    可迭代对象
    
    什么是迭代器模式？
    1. 访问聚合对象的内容，而无需暴露内部表示
    2. 支持对聚合对象的多种遍历（同一个可迭代对象可以返回多个迭代器）
    """
    def  __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
    
    # 调用iter()会得到一个迭代器对象
    def __iter__(self):
        return SentenceIterator(self.text)

class SentenceIterator():
    
    """迭代器"""
    
    """
    迭代器是可迭代的
    可迭代对象不是迭代器
    """
    def __init__(self, words):
        self.words = words
        self.index = 0
    
    # 迭代器需要实现__next__()方法，返回单个对象
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    
    # 返回迭代器本身
    def __iter__(self):
        return self
    

### Sentence第三版

class SentenceV3():
    
    """使用生成器函数"""
    
    def  __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
    
    # 生成器函数 === 生成器工厂 --> 生成器对象
    def __iter__(self):
        for word in words:
            # 和普通函数的区别，有yield关键字
            yield word
        # 可以不需要return，可以自动返回
        # return 
        
        
        
### Sentence第四版

class SentenceV4():
    
    """
    使用生成器函数，惰性实现，尽可能延后生成值（只要使用的是python3，尽可能懒惰）
    """
    
    def  __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
    
    def __iter__(self):
        # 不需要words列表了
        for word in RE_WORD.finditer(self.text):
            yield word
            
### Sentence第五版

class SentenceV5():
    
    """
    生成器表达式: 如果要写多行，建议写生成器函数
    """
    
    def  __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
    
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(text))


if __name__ == "__main__":
    
    # for隐式调用iter()，返回一个迭代器对象，并且内部会处理StopIteration异常
    s = "ABC" # 可迭代对象
    for c in s: 
        print(c)
    
    it = iter(s) # 创建一个迭代器
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break
            