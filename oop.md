# Python 编程思想

1. 基本的程序设计模式(IPO)
   - input -> process（模块化设计，拆分成更小的 IPO）-> output
2. 解决复杂问题的有效方法（自顶向下）
   - 模块化设计
     - 抽象出关键的数据结构
       - 数据输入 -> 抽象基类
       - 逻辑处理 -> 中间过程数据抽象基类
         - 分层缺失: 各种功能写在一个类里
       - 数据输出 -> 抽象基类
3. 编程思想
   - 结构化
   - 关注点分离
   - 抽象
     - 优雅的编程始于抽象（无需关注实现细节，基于提供的抽象来构建应用）
     - 在合适的抽象上去思考问题（如果有人给你提供了抽象，你就得按照人家的规定来使用，不然就有点不识好歹了，除非你牛逼自己去实现）
   - 封装
     - 封装是抽象的实现形式
     - 将功能封装成 python 的模块或 golang 的包（工具库 or 层次结构）
   - 复用
     - 没有封装就没有复用
   - 分治
     - 如果一个问题无法解决，尝试分解问题（如何解决一个问题？）
   - 组合
     - 单一逻辑能够处理的问题有限，需要组合起来
   - 缓存
   - 解耦
     - 高内聚，低耦合
4. FP or OOP

   - FP: 更适合处理无状态的少量数据，单一流程
     - 变量不可变 -> 无状态 -> 更适合执行并发操作
     - 少量的数据，大量的简短函数，很容易添加新的函数
     - 但是如果要添加数据，就很费劲
   - OOP: 更适合处理有状态的数据，复杂的数据
     - 数据和操作绑定
     - 有状态 -> 方法带来副作用(状态改变) -> 更适合和实际生活中的场景联系起来 -> 容易看懂
     - 如果一个概念，必须包含多个接口才完整，没有理由分离成一个个函数
   - OOP 中的对象，就是一个更小的程序，最重要的事情就是管理状态，并且数据和操作绑定
   - 当大量的对象组成一个系统时，我们只需关注对象之间的交互，降低耦合度，提高代码的可维护性
     - 如果没有 oop，函数都写在一起，当然也可以分成多个文件写
     - 可能会写很多的全局变量来表示不同的状态
   - 在目标的分解上，OOP 是数据驱动，FP 是操作驱动。所以在不改变源代码的前提下，可以自然地给 OOP 添加新的类型，给 FP 添加新的操作
   - FP 如何添加新的类型？因为 FP 更容易添加操作，我们可以通过添加构造函数来实现新的类型
   - OOP 如何添加新的操作？如果要添加一个新操作，新建一个 visitor 操作类（通过添加类来新增操作）
     - 一开始，我在理解，什么是数据？什么是操作？
     - 结果等理解了，才发现，数据不是数据，操作不是操作（在 golang 中，我可以把函数放到接口中）

   ```python
   # 访问者模式: 数据和操作如何分离？当我定义个 visitor 类时，shape 类增加了新的操作
   # 在 OOP 中，如果要添加一个操作，我们需要在每个类中添加一个方法，这就违反了封装原则，违背了 OOP 的核心思想
   class Shape:
       def accept(self, visitor):
           pass

   class Circle(Shape):
       def accept(self, visitor):
           visitor.visit_circle(self) # self 包含数据，visitor 包含操作

   class Rectangle(Shape):
       def accept(self, visitor):
           visitor.visit_rectangle(self)

   # 确保visitor实现了所有方法
   class Visitor:
       @abstractmethod
       def visit_circle(self, circle):
           ...

       @abstractmethod
       def visit_rectangle(self, rectangle):
           ...

    # 用于绘制图形的visitor
    class DrawVisitor(Visitor):
       def visit_circle(self, circle):
           print("Drawing a circle")

       def visit_rectangle(self, rectangle):
           print("Drawing a rectangle")

    # 用来计算面积的visitor
    class AreaCalculator(Visitor):
      def visit_circle(self, circle):
          return 3.14 * circle.radius ** 2

      def visit_rectangle(self, rectangle):
          return rectangle.width * rectangle.height

   # 客户端代码: 通过传入不同的visitor，实现不同的操作
   def draw_shapes(shapes):
       for shape in shapes:
           shape.accept(ShapeVisitor()) # shape 都有 accept 方法，通过传入不同的 visitor 实现不同的操作

   def calculate_areas(shapes):
       for shape in shapes:
           shape.accept(AreaCalculator())
   ```

   - 面对不同数据类型的交互时，FP 通过模式匹配来解决，OOP 通过双分派来解决（多态）
     - FP 通过 if-else 语句来判断类型
     - OOP 通过多态来解决

   ```python
   # 简单的多态: 如果需要添加一个计算面积的操作，需要在所有类中添加一个新方法，违背了封装原则
   class Shape:
       def draw(self):
           pass

   class Circle(Shape):
       def draw(self):
           print("Drawing a circle")

   class Rectangle(Shape):
       def draw(self):
           print("Drawing a rectangle")

   def draw_shape(shape):
       shape.draw()  # 和 golang 中的接口实现类似，虽然 shape 的类型不同，但是都有 draw 方法

   draw_shape(Circle())
   draw_shape(Rectangle())

   # 对象的交互通过方法来完成，而不是通过类型判断（多态的本质: 通过接口来限制函数签名，达到不同对象调用同一个方法，执行不同的操作）
   # 模式匹配: 通过 if-else 语句来判断类型，依据类型来执行不同的操作
   # if isinstance(shape, Circle):
   #     shape.draw_circle()
   # elif isinstance(shape, Rectangle):
   #     shape.draw_rectangle()
   ```

```python
# 函数的不可变性: 不依赖于外部状态，不会产生副作用（函数式编程应该就是这样，更适合并发场景）

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # oop本质上就是`有状态`的函数式编程
    # 数据和方法绑定，方法可以修改数据，通过self参数给方法传递数据
    # 闭包，我认为也是一种OOP的思想，让函数有状态（当函数调用会产生副作用，就可以认为是有状态的）
    def age_plus_one(self):
        self.age += 1
```
