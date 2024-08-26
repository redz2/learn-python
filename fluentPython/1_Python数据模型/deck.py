# 特殊方式是让Python解释器调用的，不需要你自己调用
# 特殊方法：magic method
# 双下方法：dunder method

import collections

# 构建少量属性，没有方法的对象，比如说一张牌
Card = collections.namedtuple('Card', ['rank', 'suit']) # 纸牌对象
# 具名元组和元组的区别：普通元组只有位置信息，具名元组有每个字段都有名称，更像一组记录

# 一摞Python风格的纸牌
# 所有类都隐式继承object
class FrenchCard():
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    
    # 为什么len()不是普通方法？
    def __len__(self):
        return len(self._cards)
    
    # 支持slice
    # 支持迭代
    def __getitem__(self, position):
        return self._cards[position]
    
    # 不要随便添加特殊方法__foo__
    
# 一副牌
deck = FrenchCard()

# 随机取出一张牌
from random import choice, shuffle
choice(deck)

# 隐式迭代
# iter(deck) -> deck.__iter__() -> 迭代器 -> __next__()
for card in deck:
    print(card)
    
# 如果没有实现__contains__()，in运算符会做一次迭代搜索
# Card("2", "spades")就是普通的new语法
Card("Q", "hearts") in deck

# 需要实现__setitem__
# shuffle(deck)

