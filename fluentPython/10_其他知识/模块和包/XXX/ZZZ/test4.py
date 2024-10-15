print("i am test4 print")

def test4():
    print("i am test4 print")
    
    
if __name__ == "__main__":
    import sys
    BASE_DIR = '/Users/tzhouyi_108087/Desktop/zhouyi/python/learn-python'
    # BASE_DIR
    # -- package1
    #    -- __init__.py
    #    -- module
    #       -- function
    #       -- class
    #       -- var
    # -- package2
    # -- package3
    # main.py
    sys.path.append(BASE_DIR)
    from cookbook.XXX.YYY import test2
    test2.say_hello()