from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=10&green=", keep_blank_values=True) # -> dict
print(my_values)
# {'red': ['5'], 'blue': [''], 'green': ['10']}

# 避免写这种特别长的表达式，不是很容易看得懂
# dict.get()获取指定key的value，不存在设置为默认值
# 空字符串，空字典以及零值都会被认为是False
print("red:         ", my_values.get("red", [""])[0] or 0)
print("green:       ", my_values.get("green", [""])[0] or 0)
print("opacity:     ", my_values.get("opacity", [""])[0] or 0) 

# 写辅助函数容易看得懂
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    res = int(found[0]) if found[0] else default
    return res
    
