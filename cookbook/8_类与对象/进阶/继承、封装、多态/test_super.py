class MyBase():
    
    def __init__(self, value):
        print("now create mybase")
        self.value = value
        
        
class PlusFive(MyBase):
    
    def __init__(self, value):
        
        super().__init__(value)
        print("now plus five")
        self.value += 5
        
class MultiplyTwo(MyBase):
    
    def __init__(self, value):
        super().__init__(value)
        print("now multiply two")
        self.value *= 2
        
class TestHerit(PlusFive, MultiplyTwo):
    
    def __init__(self, value):
        super().__init__(value)
        
print(TestHerit.__mro__)

# 深度优先，先进后出  
t = TestHerit(6)
print(t.value)
# (6*2)+5



        
        

    