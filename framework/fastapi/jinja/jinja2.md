# jinja2
1. 渲染模板字符串
```
from jinja2 import Template
# 定义模板字符串
template_string = "Hello, {{name}}"
# 创建模板对象
template = Template(template_string)
# 渲染模板
output = template.render(name="world")
print(output)
```

2. 渲染模板文件
```
from jinja2 import Environment, FileSystemLoader
# 创建一个加载器
file_loader = FileSystemLoader('path/to/templates')
# 创建一个环境对象
env = Environment(oader=file_loader)
# 加载模板文件
template = env.get_template('template_file')
# 渲染文件
output = template.render(title="Jinja2 Example", name="world")
print(output)

```